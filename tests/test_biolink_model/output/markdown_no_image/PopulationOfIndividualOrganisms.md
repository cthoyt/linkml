
# Class: population of individual organisms


A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

URI: [biolink:PopulationOfIndividualOrganisms](https://w3id.org/biolink/vocab/PopulationOfIndividualOrganisms)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[ThingWithTaxon],[StudyPopulation],[PopulationToPopulationAssociation],[ExposureEventToOutcomeAssociation]-%20has%20population%20context%200..1>[PopulationOfIndividualOrganisms&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[PopulationToPopulationAssociation]-%20object%201..1>[PopulationOfIndividualOrganisms],[PopulationToPopulationAssociation]-%20subject%201..1>[PopulationOfIndividualOrganisms],[VariantToPopulationAssociation]-%20object%201..1>[PopulationOfIndividualOrganisms],[PopulationOfIndividualOrganisms]uses%20-.->[ThingWithTaxon],[PopulationOfIndividualOrganisms]^-[StudyPopulation],[OrganismalEntity]^-[PopulationOfIndividualOrganisms],[OrganismalEntity],[OrganismTaxon],[NamedThing],[ExposureEventToOutcomeAssociation],[Attribute],[Association],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[ThingWithTaxon],[StudyPopulation],[PopulationToPopulationAssociation],[ExposureEventToOutcomeAssociation]-%20has%20population%20context%200..1>[PopulationOfIndividualOrganisms&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[PopulationToPopulationAssociation]-%20object%201..1>[PopulationOfIndividualOrganisms],[PopulationToPopulationAssociation]-%20subject%201..1>[PopulationOfIndividualOrganisms],[VariantToPopulationAssociation]-%20object%201..1>[PopulationOfIndividualOrganisms],[PopulationOfIndividualOrganisms]uses%20-.->[ThingWithTaxon],[PopulationOfIndividualOrganisms]^-[StudyPopulation],[OrganismalEntity]^-[PopulationOfIndividualOrganisms],[OrganismalEntity],[OrganismTaxon],[NamedThing],[ExposureEventToOutcomeAssociation],[Attribute],[Association],[Agent])

## Identifier prefixes

 * HANCESTRO

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixin

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

## Children

 * [StudyPopulation](StudyPopulation.md) - A group of people banded together or treated as a group as participants in a research study.

## Referenced by Class

 *  **[Association](Association.md)** *[has population context](has_population_context.md)*  <sub>0..1</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[population to population association➞object](population_to_population_association_object.md)*  <sub>1..1</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  **[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)** *[population to population association➞subject](population_to_population_association_subject.md)*  <sub>1..1</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association➞object](variant_to_population_association_object.md)*  <sub>1..1</sub>  **[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)**

## Attributes


### Inherited from organismal entity:

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

### Mixed in from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Local names:** | | population (ga4gh) |
|  | | population (agr) |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | PCO:0000001 |
|  | | SIO:001061 |
|  | | UMLSSC:T098 |
|  | | UMLSST:popg |
|  | | OBI:0000181 |
| **Narrow Mappings:** | | UMLSSC:T099 |
|  | | UMLSST:famg |
|  | | UMLSSC:T100 |
|  | | UMLSST:aggp |
|  | | UMLSSC:T101 |
|  | | UMLSST:podg |

