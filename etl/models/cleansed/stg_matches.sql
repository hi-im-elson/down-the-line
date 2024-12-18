{{ config(schema='stg', alias='matches', materialized='table') }}

with cleaned_matches as (
    select
        cast(match_id as string) as matchId,
        cast("Player 1" as string) as player1,
        cast("Player 2" as string) as player2,
        cast("Pl 1 hand" as string) as player1Hand,
        cast("Pl 2 hand" as string) as player2Hand,
        cast(strptime(cast("Date" as string), '%Y%m%d') as date) as date,
        cast(Tournament as string) as tournament,
        cast("Round" as string) as round,
        cast(Time as string) as time,
        cast(Court as string) as court,
        cast(Surface as string) as surface,
        cast(Umpire as string) as umpire,
        cast("Best of" as integer) as bestOf,
        cast("Final TB?" as string) as finalTiebreak
    from {{ source('raw', 'matches') }}
    where player1Hand is not null
)

select * 
from cleaned_matches