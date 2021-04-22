#!/bin/bash


export PGPASSWORD=1234
PRJ_PATH=/home/dbd/cs540/project



# Create table
psql -U postgres -d spatial -f $PRJ_PATH/sql/aadt_tabledef.sql

# Load data
TABLE="volusia.aadt_segments (seg_id,year_,district,cosite,roadway,desc_frm,desc_to,aadt,aadtflg,kflg,k100flg,dflg,tflg,countydot,county,mng_dist,begin_post,end_post,kfctr,k100fctr,dfctr,tfctr,shape_leng,geom)"
CSV_PATH=$PRJ_PATH/csv/volusia-aadt.csv
FORMAT="(FORMAT 'csv', DELIMITER E'\t', NULL '')"
psql -U postgres -d spatial -e -c "\COPY $TABLE FROM '$CSV_PATH' WITH $FORMAT;"


# Convert to Geom
psql -U postgres -d spatial -e -c "ALTER TABLE volusia.aadt_segments ALTER COLUMN geom TYPE geometry;"
#  USING ST_SetSRID((geom::GEOMETRY), 102258);"


# Index data
psql -U postgres -d spatial -e -c "CREATE INDEX ON volusia.aadt_segments (seg_id);"