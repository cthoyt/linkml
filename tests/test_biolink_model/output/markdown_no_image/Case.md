
# Class: case


An individual (human) organism that has a patient role in some clinical context.

URI: [biolink:Case](https://w3id.org/biolink/vocab/Case)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[IndividualOrganism],[CaseToEntityAssociationMixin],[CaseToEntityAssociationMixin]-%20subject%201..1>[Case&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[IndividualOrganism]^-[Case],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[IndividualOrganism],[CaseToEntityAssociationMixin],[CaseToEntityAssociationMixin]-%20subject%201..1>[Case&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[IndividualOrganism]^-[Case],[Attribute],[Agent])

## Parents

 *  is_a: [IndividualOrganism](IndividualOrganism.md) - An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576

## Referenced by Class

 *  **[CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)** *[case to entity association mixin➞subject](case_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[Case](Case.md)**

## Attributes


### Inherited from individual organism:

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
 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Range: [NamedThing](NamedThing.md)
 * [organismal entity➞has attribute](organismal_entity_has_attribute.md)  <sub>0..\*</sub>
     * Description: may often be an organism attribute
     * Range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | patient |
|  | | proband |

