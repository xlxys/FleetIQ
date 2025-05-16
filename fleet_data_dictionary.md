
# Fleet Synthetic Data Dictionary

This document describes the columns in the `fleet_synthetic_data.csv` file.

| Column Name                | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `vehicle_id`              | Unique identifier for the vehicle                                           |
| `trip_id`                 | Unique identifier for each trip                                            |
| `driver_id`               | Unique identifier for the driver                                           |
| `fleet_name`              | Name of the fleet the vehicle belongs to                                   |
| `start_time`              | Timestamp when the trip started                                            |
| `end_time`                | Timestamp when the trip ended                                              |
| `distance_km`            | Total distance covered during the trip (in kilometers)                      |
| `route_type`             | Type of route (urban, highway, mixed)                                       |
| `fuel_consumption`       | Amount of fuel consumed during the trip                                     |
| `fuel_efficiency_km_l`   | Fuel efficiency (kilometers per liter)                                      |
| `fuel_type`              | Type of fuel used by the vehicle                                            |
| `engine_temp_avg`        | Average engine temperature during the trip (°C)                             |
| `tire_pressure_avg`      | Average tire pressure (psi)                                                 |
| `battery_voltage_avg`    | Average battery voltage (V)                                                 |
| `engine_warnings`        | Number of engine-related warnings during the trip                           |
| `brake_warnings`         | Number of brake-related warnings during the trip                            |
| `oil_quality`            | Oil quality score (0.0 to 1.0)                                               |
| `maintenance_required`   | Indicates if maintenance is required (True/False)                           |
| `avg_speed_kmh`          | Average speed during the trip (km/h)                                        |
| `max_speed_kmh`          | Maximum speed recorded during the trip (km/h)                               |
| `harsh_braking_count`    | Number of harsh braking events                                              |
| `harsh_acceleration_count` | Number of harsh acceleration events                                       |
| `idling_time_min`        | Total idling time during the trip (minutes)                                 |
| `weather_condition`      | Weather condition during the trip (e.g., clear, rain, snow, fog)            |
| `outside_temperature`    | Outside temperature during the trip (°C)                                    |
| `road_condition`         | Road condition (dry, wet, icy)                                              |
