
# Class: genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background

URI: [biolink:Genotype](https://w3id.org/biolink/vocab/Genotype)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[OrganismTaxon],[NamedThing],[GenotypeToVariantAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeToEntityAssociationMixin],[GenotypeAsAModelOfDiseaseAssociation],[Zygosity]<has%20zygosity%200..1-++[Genotype&#124;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeAsAModelOfDiseaseAssociation]-%20subject%201..1>[Genotype],[GenotypeToEntityAssociationMixin]-%20subject%201..1>[Genotype],[GenotypeToGeneAssociation]-%20subject%201..1>[Genotype],[GenotypeToGenotypePartAssociation]-%20object%201..1>[Genotype],[GenotypeToGenotypePartAssociation]-%20subject%201..1>[Genotype],[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1>[Genotype],[GenotypeToVariantAssociation]-%20subject%201..1>[Genotype],[GenomicEntity]^-[Genotype],[GenomicEntity],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[OrganismTaxon],[NamedThing],[GenotypeToVariantAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeToEntityAssociationMixin],[GenotypeAsAModelOfDiseaseAssociation],[Zygosity]<has%20zygosity%200..1-++[Genotype&#124;has_biological_sequence(i):biological_sequence%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeAsAModelOfDiseaseAssociation]-%20subject%201..1>[Genotype],[GenotypeToEntityAssociationMixin]-%20subject%201..1>[Genotype],[GenotypeToGeneAssociation]-%20subject%201..1>[Genotype],[GenotypeToGenotypePartAssociation]-%20object%201..1>[Genotype],[GenotypeToGenotypePartAssociation]-%20subject%201..1>[Genotype],[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1>[Genotype],[GenotypeToVariantAssociation]-%20subject%201..1>[Genotype],[GenomicEntity]^-[Genotype],[GenomicEntity],[Attribute],[Agent])

## Identifier prefixes

 * ZFIN
 * FB

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by Class

 *  **[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md)** *[genotype as a model of disease association➞subject](genotype_as_a_model_of_disease_association_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md)** *[genotype to entity association mixin➞subject](genotype_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association➞subject](genotype_to_gene_association_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)** *[genotype to phenotypic feature association➞subject](genotype_to_phenotypic_feature_association_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞subject](genotype_to_variant_association_subject.md)*  <sub>1..1</sub>  **[Genotype](Genotype.md)**

## Attributes


### Own

 * [has zygosity](has_zygosity.md)  <sub>0..1</sub>
     * Range: [Zygosity](Zygosity.md)

### Inherited from genomic entity:

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
 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Consider renaming as genotypic entity |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | GENO:0000536 |
|  | | SIO:001079 |

