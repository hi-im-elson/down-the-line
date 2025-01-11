# Down The Line

Down The Line is a tennis analytics project designed to provide in-depth data analysis and insights for tennis enthusiasts, players, and analysts. The project combines match statistics with advanced analytics to identify trends, player tendencies, and key match dynamics. 

This project leverages data from the [Match Charting Project](https://github.com/JeffSackmann/tennis_MatchChartingProject), maintained by Jeff Sackmann. Their work in collecting and organizing detailed tennis match data is foundational to this project. Many thanks to Jeff and the contributors to the Match Charting Project for their incredible efforts! 

## Features
* Rallies: Analysis of every shot a player receives (Forehand vs Backhand), the player's preference in return direction (Cross court, down the line, down the middle), and their effectiveness [In Progress]
* Serve: Aggregations of where a player serves and how influential their serve is in winning the point
* Competitions: Overall success as a player including performance by surface

## Tools and Frameworks
### Current
* polars: Package to read CSV files and write to Parquet. Leveraging the underlying PyArrow engine in a Spark-like syntax
* DuckDB: In-memory data warehouse for high-performance, small-scale analytics use cases
* dbt (core): SQL transformation layer leveraging Jinja to create highly-organized ETL and analytics engineering scripts
* Plotly Dash: Python-based web application used to render interactive graphs based on the popular and aesthetic (in my opinion) Plotly library

### Future
* S3/ADLS/Cloud Storage: Cloud-based blob storage service instead of a local `data` folder to store raw and intermediate transformations
* Apache Iceberg: Open-table format to manage parquet metadata
* EC2/VM/Compute: Cloud-based single instance virtual machine to host the small-scale application

## Data
The core idea in managing the data is to follow the Medallion architecture, preserving the original data while each layer of transformation makes data more accessible for downstream applications and users.

* Raw Data: Jeff Sackmann's GitHub project is forked and CSV files are copied into a local directory
* Silver Data 1 (Data Lake): Data is converted into a Parquet format for greater compatibility with open-table formats like Apache Iceberg. 
* Silver Data 2 (Data Warehouse - View): Parquet data is then read into a DuckDB database where all fields, except dates, are converted into strings to preserve as much of the original data. Field names are modified to follow a standardized naming convention for readability.
* Silver Data 3 (Data Warehouse - View): A dbt model is then used to select the relevant fields, perform type casting to ensure field types are meaningful, and basic cleansing where relevant.
* Gold Data (Data Warehouse - Table): A dbt model then aggregates and joins the silver tables to create end tables relevant to the analysis or report required. This is persisted to reduce time to populate and modify the graphs in the user-facing application.

## License

This project is licensed under the GNU AGPL License.

The software is provided "as is," without warranty of any kind.

For full license details, refer to the LICENSE file in this repository.