
# Class: book chapter




URI: [biolink:BookChapter](https://w3id.org/biolink/vocab/BookChapter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[Publication]^-[BookChapter&#124;published_in:uriorcurie;volume:string%20%3F;chapter:string%20%3F;authors(i):string%20*;pages(i):string%20*;summary(i):string%20%3F;keywords(i):string%20*;mesh_terms(i):uriorcurie%20*;xref(i):iri_type%20*;id(i):string;name(i):label_type%20%3F;type(i):string;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;iri(i):iri_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[Publication]^-[BookChapter&#124;published_in:uriorcurie;volume:string%20%3F;chapter:string%20%3F;authors(i):string%20*;pages(i):string%20*;summary(i):string%20%3F;keywords(i):string%20*;mesh_terms(i):uriorcurie%20*;xref(i):iri_type%20*;id(i):string;name(i):label_type%20%3F;type(i):string;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;iri(i):iri_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Attribute],[Agent])

## Parents

 *  is_a: [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.

## Referenced by Class


## Attributes


### Own

 * [book chapter➞published in](book_chapter_published_in.md)  <sub>1..1</sub>
     * Description: The enclosing parent book containing the chapter should have industry-standard identifier from ISBN.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [volume](volume.md)  <sub>0..1</sub>
     * Description: volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication
     * Range: [String](types/String.md)
 * [chapter](chapter.md)  <sub>0..1</sub>
     * Description: chapter of a book
     * Range: [String](types/String.md)

### Inherited from publication:

 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
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
 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rights](rights.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>0..1</sub>
     * Description: date on which an entity was created. This can be applied to nodes or edges
     * Range: [Date](types/Date.md)
 * [authors](authors.md)  <sub>0..\*</sub>
     * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
     * Range: [String](types/String.md)
 * [publication➞pages](publication_pages.md)  <sub>0..\*</sub>
     * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
     * Range: [String](types/String.md)
 * [summary](summary.md)  <sub>0..1</sub>
     * Description: executive  summary of a publication
     * Range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..\*</sub>
     * Description: keywords tagging a publication
     * Range: [String](types/String.md)
 * [mesh terms](mesh_terms.md)  <sub>0..\*</sub>
     * Description: mesh terms tagging a publication
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: Alternate CURIEs for a thing
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal)
 * [publication➞id](publication_id.md)  <sub>1..1</sub>
     * Description: Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.
     * Range: [String](types/String.md)
 * [publication➞name](publication_name.md)  <sub>0..1</sub>
     * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
     * Range: [LabelType](types/LabelType.md)
 * [publication➞type](publication_type.md)  <sub>1..1</sub>
     * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |

