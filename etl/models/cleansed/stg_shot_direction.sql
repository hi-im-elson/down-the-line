{{ config(schema='stg', alias='shot_direction', materialized='table') }}

with cleaned_shot_direction as (
    select
        cast(match_id as string) as matchId,
        cast(strptime(left(match_id, 8), '%Y%m%d') as date) as matchDate,
        cast(player as string) as player,
        cast(row as string) as shotType,
        cast(shots as integer) as shotCount,
        cast(pt_ending as integer) as ptEnding,
        cast(winners as integer) as winners,
        cast(induced_forced as integer) as inducedForcedErrors,
        cast(unforced as integer) as commitedUnforcedErrors,
        cast(shots_in_pts_won as integer) as shotsWon,
        cast(shots_in_pts_lost as integer) as shotsLost,
        
    from {{ source('raw', 'shot_direction') }}
)

select * 
from cleaned_shot_direction