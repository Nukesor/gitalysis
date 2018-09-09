# Gitalysis

Gitalysis is the analysis tool for data collected by [Gitalizer](https://github.com/Nukesor/gitalysi://github.com/Nukesor/gitalizer).

Gitalysis can be capable of:
- Tracking the location of a targeted git user via their open source contributions.
- Detect holiday and sick leave in your commit pattern as well as other anomalies.
- Draw punchcards in the old Github style, which provide insight into the sleeping and working rhythm of a person.

## Results:

Image from home location and travel path analysis:
<p align="center">
    <img src="https://raw.githubusercontent.com/Nukesor/images/master/gitalizer_map.png">
</p>

Holiday/sick leave and other anomaly analysis:
<p align="center">
    <img src="https://raw.githubusercontent.com/Nukesor/images/master/gitalizer_holiday.png">
</p>

Sleep rhythm and working hour analysis:
<p align="center">
    <img src="https://raw.githubusercontent.com/Nukesor/images/master/gitalizer_punchcard.png">
</p>


## Cli
**DB** related:
- `gitalizer db initdb` Initializes a new database with schema and populates the timezone database
- `gitalizer db build_time_db` Rebuild the timezone database (needed if a new version was released)

**Scanning**:

- `gitalizer plot user [login]` Plot all graphs for a specific github user.
- `gitalizer plot user_for_repositories [login] [repositories...]` Get statistics of an user for specific repositories.
- `gitalizer plot comparison [logins...] [repositories...]` Get statistics of several user for specific repositories

**analyse**:
- `gitalizer analyse punchcard` Delete a repository with all it's commit
- `gitalizer analyse travel` Delete a repository with all it's commit
