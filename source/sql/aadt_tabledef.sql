drop table if exists volusia.aadt_segments;

create table volusia.aadt_segments (
    seg_id      double precision,
    year_       double precision,
    district    text,
    cosite      text,
    roadway     text,
    desc_frm    text,
    desc_to     text,
    aadt        double precision,
    aadtflg     text,
    kflg        text,
    k100flg     text,
    dflg        text,
    tflg        text,
    countydot   text,
    county      text,
    mng_dist    text,
    begin_post  double precision,
    end_post    double precision,
    kfctr       double precision,
    k100fctr    double precision,
    dfctr       double precision,
    tfctr       double precision,
    shape_leng  double precision,
    geom        text
);