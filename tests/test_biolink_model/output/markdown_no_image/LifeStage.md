
# Class: life stage


A stage of development or growth of an organism, including post-natal adult stages

URI: [biolink:LifeStage](https://w3id.org/biolink/vocab/LifeStage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismalEntity],[OrganismTaxon],[NamedThing],[GeneToExpressionSiteAssociation]-%20stage%20qualifier%200..1>[LifeStage&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GeneExpressionMixin]-%20stage%20qualifier%200..1>[LifeStage],[GeneToExpressionSiteAssociation]-%20stage%20qualifier(i)%200..1>[LifeStage],[LifeStage]uses%20-.->[ThingWithTaxon],[OrganismalEntity]^-[LifeStage],[GeneToExpressionSiteAssociation],[GeneExpressionMixin],[Attribute],[Association],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismalEntity],[OrganismTaxon],[NamedThing],[GeneToExpressionSiteAssociation]-%20stage%20qualifier%200..1>[LifeStage&#124;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GeneExpressionMixin]-%20stage%20qualifier%200..1>[LifeStage],[GeneToExpressionSiteAssociation]-%20stage%20qualifier(i)%200..1>[LifeStage],[LifeStage]uses%20-.->[ThingWithTaxon],[OrganismalEntity]^-[LifeStage],[GeneToExpressionSiteAssociation],[GeneExpressionMixin],[Attribute],[Association],[Agent])

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixin

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

## Referenced by Class

 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)*  <sub>0..1</sub>  **[LifeStage](LifeStage.md)**
 *  **[Association](Association.md)** *[stage qualifier](stage_qualifier.md)*  <sub>0..1</sub>  **[LifeStage](LifeStage.md)**

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
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | UBERON:0000105 |
| **Narrow Mappings:** | | HsapDv:0000000 |

