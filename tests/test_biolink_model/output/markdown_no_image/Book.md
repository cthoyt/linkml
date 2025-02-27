
# Class: book


This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.

URI: [biolink:Book](https://w3id.org/biolink/vocab/Book)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[Publication]^-[Book&#124;id:string;type:string;authors(i):string%20*;pages(i):string%20*;summary(i):string%20%3F;keywords(i):string%20*;mesh_terms(i):uriorcurie%20*;xref(i):iri_type%20*;name(i):label_type%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;iri(i):iri_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[Publication]^-[Book&#124;id:string;type:string;authors(i):string%20*;pages(i):string%20*;summary(i):string%20%3F;keywords(i):string%20*;mesh_terms(i):uriorcurie%20*;xref(i):iri_type%20*;name(i):label_type%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;iri(i):iri_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Attribute],[Agent])

## Identifier prefixes

 * isbn
 * NLMID

## Parents

 *  is_a: [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.

## Referenced by Class


## Attributes


### Own

 * [book➞id](book_id.md)  <sub>1..1</sub>
     * Description: Books should have industry-standard identifier such as from ISBN.
     * Range: [String](types/String.md)
 * [book➞type](book_type.md)  <sub>1..1</sub>
     * Description: Should generally be set to an ontology class defined term for 'book'.
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
 * [publication➞name](publication_name.md)  <sub>0..1</sub>
     * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
     * Range: [LabelType](types/LabelType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |

