
# Class: pathological process


A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.

URI: [biolink:PathologicalProcess](https://w3id.org/biolink/vocab/PathologicalProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[PathologicalProcessOutcome],[PathologicalProcessExposure],[PathologicalProcess&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F]uses%20-.->[PathologicalEntityMixin],[PathologicalProcess]^-[PathologicalProcessOutcome],[PathologicalProcess]^-[PathologicalProcessExposure],[BiologicalProcess]^-[PathologicalProcess],[PathologicalEntityMixin],[NamedThing],[BiologicalProcess],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[PathologicalProcessOutcome],[PathologicalProcessExposure],[PathologicalProcess&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F]uses%20-.->[PathologicalEntityMixin],[PathologicalProcess]^-[PathologicalProcessOutcome],[PathologicalProcess]^-[PathologicalProcessExposure],[BiologicalProcess]^-[PathologicalProcess],[PathologicalEntityMixin],[NamedThing],[BiologicalProcess],[Attribute],[Agent])

## Parents

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions

## Uses Mixin

 *  mixin: [PathologicalEntityMixin](PathologicalEntityMixin.md) - A pathological (abnormal) structure or process.

## Children

 * [PathologicalProcessExposure](PathologicalProcessExposure.md) - A pathological process, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease.
 * [PathologicalProcessOutcome](PathologicalProcessOutcome.md) - An outcome resulting from an exposure event which is the manifestation of a pathological process.

## Referenced by Class


## Attributes


### Inherited from biological process:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)
 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Range: [NamedThing](NamedThing.md)
 * [has input](has_input.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)
 * [enabled by](enabled_by.md)  <sub>0..\*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * Range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:1110122 |
|  | | NCIT:C16956 |
| **Narrow Mappings:** | | NCIT:C19151 |
|  | | EFO:0009708 |

