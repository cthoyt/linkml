
# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [biolink:SequenceVariant](https://w3id.org/biolink/vocab/SequenceVariant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToEntityAssociationMixin],[VariantAsAModelOfDiseaseAssociation],[Snv],[SequenceVariantModulatesTreatmentAssociation],[Gene]<has%20gene%200..*-%20[SequenceVariant&#124;has_biological_sequence:biological_sequence%20%3F;id:string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeToVariantAssociation]-%20object%201..1>[SequenceVariant],[SequenceVariantModulatesTreatmentAssociation]-%20subject%201..1>[SequenceVariant],[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1>[SequenceVariant],[VariantAsAModelOfDiseaseAssociation]-%20subject%201..1>[SequenceVariant],[VariantToEntityAssociationMixin]-%20subject%201..1>[SequenceVariant],[VariantToPhenotypicFeatureAssociation]-%20subject%201..1>[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1>[SequenceVariant],[SequenceVariant]^-[Snv],[GenomicEntity]^-[SequenceVariant],[OrganismTaxon],[NamedThing],[GenotypeToVariantAssociation],[GenomicEntity],[GeneHasVariantThatContributesToDiseaseAssociation],[Gene],[Attribute],[Association],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToEntityAssociationMixin],[VariantAsAModelOfDiseaseAssociation],[Snv],[SequenceVariantModulatesTreatmentAssociation],[Gene]<has%20gene%200..*-%20[SequenceVariant&#124;has_biological_sequence:biological_sequence%20%3F;id:string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenotypeToVariantAssociation]-%20object%201..1>[SequenceVariant],[SequenceVariantModulatesTreatmentAssociation]-%20subject%201..1>[SequenceVariant],[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%200..1>[SequenceVariant],[VariantAsAModelOfDiseaseAssociation]-%20subject%201..1>[SequenceVariant],[VariantToEntityAssociationMixin]-%20subject%201..1>[SequenceVariant],[VariantToPhenotypicFeatureAssociation]-%20subject%201..1>[SequenceVariant],[VariantToPopulationAssociation]-%20subject%201..1>[SequenceVariant],[SequenceVariant]^-[Snv],[GenomicEntity]^-[SequenceVariant],[OrganismTaxon],[NamedThing],[GenotypeToVariantAssociation],[GenomicEntity],[GeneHasVariantThatContributesToDiseaseAssociation],[Gene],[Attribute],[Association],[Agent])

## Identifier prefixes

 * CAID
 * CLINVAR
 * ClinVarVariant
 * WIKIDATA
 * DBSNP
 * DBSNP
 * MGI
 * ZFIN
 * FB
 * WB
 * WormBase

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Children

 * [Snv](Snv.md) - SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist

## Referenced by Class

 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[genotype to variant association➞object](genotype_to_variant_association_object.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[Association](Association.md)** *[sequence variant qualifier](sequence_variant_qualifier.md)*  <sub>0..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md)** *[variant as a model of disease association➞subject](variant_as_a_model_of_disease_association_subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)** *[variant to entity association mixin➞subject](variant_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)** *[variant to phenotypic feature association➞subject](variant_to_phenotypic_feature_association_subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**
 *  **[VariantToPopulationAssociation](VariantToPopulationAssociation.md)** *[variant to population association➞subject](variant_to_population_association_subject.md)*  <sub>1..1</sub>  **[SequenceVariant](SequenceVariant.md)**

## Attributes


### Own

 * [sequence variant➞has gene](sequence_variant_has_gene.md)  <sub>0..\*</sub>
     * Description: Each allele can be associated with any number of genes
     * Range: [Gene](Gene.md)
 * [sequence variant➞has biological sequence](sequence_variant_has_biological_sequence.md)  <sub>0..1</sub>
     * Description: The state of the sequence w.r.t a reference sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)
 * [sequence variant➞id](sequence_variant_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: ZFIN:ZDB-ALT-980203-1091 ti282a allele from ZFIN
     * Example: ClinVarVariant:17681 NM_007294.3(BRCA1):c.2521C>T (p.Arg841Trp)

### Inherited from genomic entity:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | allele |
| **Local names:** | | allele (agr) |
| **Alt Descriptions:** | | An entity that describes a single affected, endogenous allele. These can be of any type that matches that definition (AGR) |
|  | | A contiguous change at a Location (VMC) |
| **Comments:** | | This class is for modeling the specific state at a locus. A single DBSNP rs ID could correspond to more than one sequence variants (e.g CIViC:1252 and CIViC:1253, two distinct BRCA2 alleles for rs28897743) |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | GENO:0000002 |
|  | | WIKIDATA:Q15304597 |
|  | | SIO:010277 |
|  | | VMC:Allele |
|  | | SO:0001059 |
| **Broad Mappings:** | | SO:0001060 |

