
# Class: activity


a provence-generating activity

URI: [ks:Activity](https://w3id.org/linkml/tests/kitchen_sink/Activity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Agent],[Agent]<was%20associated%20with%200..1-%20[Activity&#124;id:string;started_at_time:date%20%3F;ended_at_time:date%20%3F;used:string%20%3F;description:string%20%3F],[Activity]<was%20informed%20by%200..1-%20[Activity],[Dataset]++-%20activities%200..*>[Activity],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Agent],[Agent]<was%20associated%20with%200..1-%20[Activity&#124;id:string;started_at_time:date%20%3F;ended_at_time:date%20%3F;used:string%20%3F;description:string%20%3F],[Activity]<was%20informed%20by%200..1-%20[Activity],[Dataset]++-%20activities%200..*>[Activity],[Dataset])

## Referenced by Record

 *  **None** *[activity set](activity_set.md)*  <sub>0..\*</sub>  **[Activity](Activity.md)**
 *  **None** *[➞activities](dataset__activities.md)*  <sub>0..\*</sub>  **[Activity](Activity.md)**
 *  **None** *[was generated by](was_generated_by.md)*  <sub>0..1</sub>  **[Activity](Activity.md)**
 *  **None** *[was informed by](was_informed_by.md)*  <sub>0..1</sub>  **[Activity](Activity.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](String.md)
 * [started at time](started_at_time.md)  <sub>0..1</sub>
     * Range: [Date](Date.md)
 * [ended at time](ended_at_time.md)  <sub>0..1</sub>
     * Range: [Date](Date.md)
 * [was informed by](was_informed_by.md)  <sub>0..1</sub>
     * Range: [Activity](Activity.md)
 * [was associated with](was_associated_with.md)  <sub>0..1</sub>
     * Range: [Agent](Agent.md)
 * [used](used.md)  <sub>0..1</sub>
     * Range: [String](String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | prov:Activity |

