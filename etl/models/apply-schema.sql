{{ config(materialized='table') }}

with matches as (
    select
        match_id
    from {{ source('js_tennis', 'raw_matches') }}
)

select * 
from matches