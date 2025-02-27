import click
from linkml.utils import validation
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.schemaview import SchemaView

from linkml.generators.pythongen import PythonGenerator
from linkml.utils.datautils import dumpers_loaders, _get_format, get_loader, _get_context, infer_index_slot, \
    infer_root_class, _is_xsv, get_dumper


@click.command()
@click.option("--module", "-m",
              help="Path to python datamodel module")
@click.option("--output", "-o",
              help="Path to output file")
@click.option("--input-format", "-f",
              type=click.Choice(list(dumpers_loaders.keys())),
              help="Input format. Inferred from input suffix if not specified")
@click.option("--output-format", "-t",
              type=click.Choice(list(dumpers_loaders.keys())),
              help="Output format. Inferred from output suffix if not specified")
@click.option("--target-class", "-C",
              help="name of class in datamodel that the root node instantiates")
@click.option("--index-slot", "-S",
              help="top level slot. Required for CSV dumping/loading")
@click.option("--schema", "-s",
              help="Path to schema specified as LinkML yaml")
@click.option("--validate/--no-validate",
              default=True,
              help="Validate against the schema")
@click.option("--context", "-c",
              multiple=True,
              help="path to JSON-LD context file. Required for RDF input/output")
@click.argument("input")
def cli(input, module, target_class, context=None, output=None, input_format=None, output_format=None,
        schema=None, validate=None, index_slot=None) -> None:
    """
    Converts instance data to and from different LinkML Runtime serialization formats.

    The instance data must conform to a LinkML model, and there must be python dataclasses
    generated from that model. The converter works by first using a linkml-runtime loader to
    instantiate in-memory model objects, then dumpers are used to serialize.
    When converting to or from RDF, a JSON-lD context must also be passed
    """
    if module is None:
        if schema is None:
            raise Exception('must pass one of module OR schema')
        else:
            python_module = PythonGenerator(schema).compile_module()
    else:
        python_module = compile_python(module)
    if schema is not None:
        sv = SchemaView(schema)
    if target_class is None:
        target_class = infer_root_class(sv)
    if target_class is None:
        raise Exception(f'target class not specified and could not be inferred')
    py_target_class = python_module.__dict__[target_class]
    input_format = _get_format(input, input_format)
    loader = get_loader(input_format)

    inargs = {}
    outargs = {}
    if input_format == 'rdf':
        if len(context) == 0:
            if schema is not None:
                context = [_get_context(schema)]
            else:
                raise Exception('Must pass in context OR schema for RDF output')
        inargs['contexts'] = list(context)[0]
    if _is_xsv(input_format):
        if index_slot is None:
            index_slot = infer_index_slot(sv, target_class)
            if index_slot is None:
                raise Exception('--index-slot is required for CSV input')
        inargs['index_slot'] = index_slot
        inargs['schema'] = schema
    obj = loader.load(source=input,  target_class=py_target_class, **inargs)
    if validate:
        if schema is None:
            raise Exception('--schema must be passed in order to validate. Suppress with --no-validate')
        # TODO: use validator framework
        validation.validate_object(obj, schema)

    output_format = _get_format(output, output_format, default='json')
    if output_format == 'rdf':
        if len(context) == 0:
            if schema is not None:
                context = [_get_context(schema)]
            else:
                raise Exception('Must pass in context OR schema for RDF output')
        outargs['contexts'] = list(context)
    if _is_xsv(output_format):
        if index_slot is None:
            index_slot = infer_index_slot(sv, target_class)
            if index_slot is None:
                raise Exception('--index-slot is required for CSV output')
        outargs['index_slot'] = index_slot
        outargs['schema'] = schema
    dumper = get_dumper(output_format)
    if output is not None:
        dumper.dump(obj, output, **outargs)
    else:
        print(dumper.dumps(obj, **outargs))


if __name__ == '__main__':
    cli(sys.argv[1:])