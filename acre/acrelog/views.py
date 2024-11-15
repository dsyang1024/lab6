from django.shortcuts import render
from .models import event, location, log, operation, operator, seed, fertilizer, spray
# Create your views here.
from django.http import HttpResponse
from django.http import Http404

import geojson
import shapely.wkt as wkt  
import shapely.geometry as geo
import geopandas as gpd
import pandas as pd


def index(request):
    latest_fields = location.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'index.html', context)



def fields(request, location_id):
    logs = log.objects.filter(location=location_id)
    print (logs)
    field = location.objects.get(pk=location_id)
    
    context = {'field':field, 'logs': logs}

    return render(request, 'fields.html', context)



def render_map(request):
    # Specify the path to your Parquet file
    parquet_file = 'data/acre_geometry.parquet'
    # Load the Parquet file with Pandas
    df = gpd.read_parquet(parquet_file)

    # Convert the DataFrame to a GeoDataFrame with GeoPandas
    gdf = gpd.GeoDataFrame(df, geometry='geometry')
    print (gdf.columns.tolist())
    print ('>>> Total data length::', len(gdf))

    # Create a GeoJSON FeatureCollection
    data = geojson.FeatureCollection([])
    # Loop through each row in the GeoDataFrame
    for index, row in gdf.iterrows():
        # add each polygon to the geojson
        # search last operation at the field from the db.sqlite3 using the row['Field'] value from the log table
        print('>>> searching :: ',row['Field'])
        try:
            last_loc = str(location.objects.get(location_name = row['Field']).id)
            last_op = log.objects.filter(location = int(last_loc))
            # order last_op by date column
            last_op = last_op.order_by('date')
            # get the last item from last_op
            last_op = last_op.last()
            # get the last operation date
            last_opday = last_op.date
            last_opday = last_opday.strftime('%Y-%m-%d')
            # get the last operation name
            last_op = last_op.event.pk
        except:
            print('    *** Error::', row['Field'],' Not found')
            lost_loc = '999'
            last_op = 'No Data'


        # convert last operation to string
        if last_op == 1:
            last_op = 'Spray/Spreading'
        elif last_op == 2:
            last_op = 'Tillage'
        elif last_op == 3:
            last_op = 'Planting'
        elif last_op == 4:
            last_op = 'Havesting'
        elif last_op == 5:
            last_op = 'Soil Sampling'

        print('>>> Last operation::', last_opday, ':', last_op)
        polygon = geo.Polygon(row['geometry'])
        marker = geojson.Feature(geometry=polygon,
                                 properties={"message":
                                             '<p class="text-center">'+
                                             'Field :: ' + str(row['Field']) + '<br>'+
                                             'Crop :: ' + str(row['2022_Crop']) + '<br>'+
                                             'Last Operation :: <strong>' + last_opday + ':' + last_op+'</strong><br>'+
                                             '<a class="btn btn-outline-danger btn-sm" href="/acrelog/'+last_loc+'/">Details</a></p>'
                                             })
        data['features'].append(marker)

    return render(request, "map.html", {"data": data})
