
# Class: exposure event to outcome association


An association between an exposure event and an outcome.

URI: [biolink:ExposureEventToOutcomeAssociation](https://w3id.org/biolink/vocab/ExposureEventToOutcomeAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[PopulationOfIndividualOrganisms],[OntologyClass],[NamedThing],[PopulationOfIndividualOrganisms]<has%20population%20context%200..1-%20[ExposureEventToOutcomeAssociation&#124;has_temporal_context:time_type%20%3F;predicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20*;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ExposureEventToOutcomeAssociation]uses%20-.->[ExposureEventToEntityAssociationMixin],[ExposureEventToOutcomeAssociation]uses%20-.->[EntityToOutcomeAssociationMixin],[Association]^-[ExposureEventToOutcomeAssociation],[ExposureEventToEntityAssociationMixin],[EntityToOutcomeAssociationMixin],[Attribute],[Association],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[PopulationOfIndividualOrganisms],[OntologyClass],[NamedThing],[PopulationOfIndividualOrganisms]<has%20population%20context%200..1-%20[ExposureEventToOutcomeAssociation&#124;has_temporal_context:time_type%20%3F;predicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20*;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ExposureEventToOutcomeAssociation]uses%20-.->[ExposureEventToEntityAssociationMixin],[ExposureEventToOutcomeAssociation]uses%20-.->[EntityToOutcomeAssociationMixin],[Association]^-[ExposureEventToOutcomeAssociation],[ExposureEventToEntityAssociationMixin],[EntityToOutcomeAssociationMixin],[Attribute],[Association],[Agent])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixin

 *  mixin: [ExposureEventToEntityAssociationMixin](ExposureEventToEntityAssociationMixin.md) - An association between some exposure event and some entity.
 *  mixin: [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) - An association between some entity and an outcome

## Attributes


### Own

 * [has population context](has_population_context.md)  <sub>0..1</sub>
     * Description: a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association.
     * Range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [has temporal context](has_temporal_context.md)  <sub>0..1</sub>
     * Description: a constraint of time placed upon the truth value of an association.
     * Range: [TimeType](types/TimeType.md)

### Inherited from association:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
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
 * [subject](subject.md)  <sub>1..1</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>1..1</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>1..1</sub>
     * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>0..1</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: connects an association to publications supporting the association
     * Range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>0..1</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * Range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..\*</sub>
     * Range: [CategoryType](types/CategoryType.md)
