select 
	volusia.gis_parcels.pid,volusia.gis_parcels.geom,rank_,aadt
from 
	volusia.gis_parcels
join
	(
		select * from volusia.addr_aadt
		join volusia.aadt_segments 
		on volusia.addr_aadt.seg_id = volusia.aadt_segments.seg_id
	) as segs
on
	volusia.gis_parcels.pid = segs.pid;