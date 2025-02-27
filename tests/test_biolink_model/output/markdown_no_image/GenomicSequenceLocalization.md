
# Class: genomic sequence localization


A relationship between a sequence feature and a genomic entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig.

URI: [biolink:GenomicSequenceLocalization](https://w3id.org/biolink/vocab/GenomicSequenceLocalization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceAssociation],[Publication],[OntologyClass],[GenomicEntity]<object%201..1-%20[GenomicSequenceLocalization&#124;start_interbase_coordinate:integer%20%3F;end_interbase_coordinate:integer%20%3F;genome_build:string%20%3F;strand:string%20%3F;phase:string%20%3F;predicate:predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20*;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenomicEntity]<subject%201..1-%20[GenomicSequenceLocalization],[SequenceAssociation]^-[GenomicSequenceLocalization],[GenomicEntity],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceAssociation],[Publication],[OntologyClass],[GenomicEntity]<object%201..1-%20[GenomicSequenceLocalization&#124;start_interbase_coordinate:integer%20%3F;end_interbase_coordinate:integer%20%3F;genome_build:string%20%3F;strand:string%20%3F;phase:string%20%3F;predicate:predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20*;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GenomicEntity]<subject%201..1-%20[GenomicSequenceLocalization],[SequenceAssociation]^-[GenomicSequenceLocalization],[GenomicEntity],[Attribute],[Agent])

## Parents

 *  is_a: [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a genomic entity it is localized to.

## Referenced by Class


## Attributes


### Own

 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>0..1</sub>
     * Description: The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on.
     * Range: [Integer](types/Integer.md)
 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>0..1</sub>
     * Description: The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on.
     * Range: [Integer](types/Integer.md)
 * [genome build](genome_build.md)  <sub>0..1</sub>
     * Description: The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
     * Range: [String](types/String.md)
 * [strand](strand.md)  <sub>0..1</sub>
     * Description: The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
     * Range: [String](types/String.md)
 * [phase](phase.md)  <sub>0..1</sub>
     * Description: The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
     * Range: [String](types/String.md)
 * [genomic sequence localization➞subject](genomic_sequence_localization_subject.md)  <sub>1..1</sub>
     * Range: [GenomicEntity](GenomicEntity.md)
 * [genomic sequence localization➞object](genomic_sequence_localization_object.md)  <sub>1..1</sub>
     * Range: [GenomicEntity](GenomicEntity.md)
 * [genomic sequence localization➞predicate](genomic_sequence_localization_predicate.md)  <sub>1..1</sub>
     * Range: [PredicateType](types/PredicateType.md)

### Inherited from sequence association:

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
