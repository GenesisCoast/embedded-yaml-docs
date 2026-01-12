[![pypi publish](https://github.com/GenesisCoast/embedded-yaml-docs/actions/workflows/python-publish.yml/badge.svg)](https://github.com/GenesisCoast/embedded-yaml-docs/actions/workflows/python-publish.yml) [![PyPI version](https://badge.fury.io/py/embedded-yaml-docs.svg)](https://badge.fury.io/py/embedded-yaml-docs)

<h3>
  
```
Embedded...
__  _____    __  _____       ____                 
\ \/ /   |  /  |/  / /      / __ \____  __________
 \  / /| | / /|_/ / /      / / / / __ \/ ___/ ___/
 / / ___ |/ /  / / /___   / /_/ / /_/ / /__(__  ) 
/_/_/  |_/_/  /_/_____/  /_____/\____/\___/____/                   
```
  
</h3>

Embedded YAML docs is a CLI tool for generating documentation about a YAML file, using code doc comments. 

This is incredibly useful for YAML pipelines/templates and additional configuration files. Where you may want to automatically generate easily readable documentation, depending on the contents of the file.

For example when the preview command is on the YAML section (left) it will output the all the comments under the property `docs` (right). The generation command works similarly except instead of outputting the YAML it is piped into the Jinja2 templating engine.

<table align="center">
<tr>
<td>
<br>
  
```
parameters:
- name: resourceGroupName
  type: string
  # Description:
  #   Resource group name.
```
  
</td>
<td>
  ➡️
</td>
<td>
<br>

```
parameters:
- name: resourceGroupName
  type: string
  docs:
    Description: Resource group name.
```

</td>
</tr>
</table>

# Installation

## From PyPi

Currently this CLI does not support Jinja v3. A fix for other versions of Jinja2 will be released with the new CLI version.

You can make sure you have the correct version of Jinja installed, by running the following command prior to installing the CLI.

```
pip3 install "Jinja2>=2.11.2,<3.0.0"
```

The tool can be installed by running:

```
pip install embedded-yaml-docs
```

Or localled by using `pip install .` when your in the same directory as `setup.py`.

## Locally

If you want to run the latest and greatest you can do so with the following steps:

1. Open a command prompt as administrator.

2. Change the current path in the command prompt to the root of the solution.

3. Run `pip install -r requirements.txt`.

4. Run `python 'setup.py' install`.

5. Run the CLI normally, the latest code should be added to your `$PATH` using the alias `embedded-yaml-docs`.

Alternatively, if you open the solution in Visual Studio (as administrator) you can use the `Python: Install & Run CLI` command to automatically do the above steps.

Each time the code is changed you will need to re-run above to force the installed CLI to update.

# Commands

Below is a short explanation of the various CLI commands that are available.

## Generate

The `generate` command is used to generate the documentation from the specified YAML files.

### File

The `generate file` command generates the documentation for a single YAML file.

```
> embedded-yaml-docs generate file [OPTIONS]
```

The following options can be supplied for the `generate file` command.

| Option | Required | Description |
|--------|----------|-------------|
| `-f, --file` | True | File path to the YAML file; to generate the documentation for. |
| `-t, --template` | True | File path to the Jinja2 template thats used in the documentation generation. |
| `-o, --output` | False | File path specifying the location and name of the documentation file that will be outputted. If no value is supplied, then the file path supplied using `-f, --file` will be used. Alongwith the extension changed from `.yml` to `.md`. |
| `-pre, --exclprefix` | False | List of comment prefixes to search for when generating the documentation. If a prefix is matched, then the corresponding documentation is excluded. To specify multiple prefixes to be excluded repeat the option identifier `-pre, --exclprefix`. |
| `-r, --root` | False | The root folder of your file structure. This is used to calculate relative paths for the YAML files. You could use this to pass your respoitory root meaning that the YAML files, will be relative to the repository. Rather than your file system. |
| `x, --exit` | False | Flag with forces the CLI to stop execution after an error. If this flag is not passed then the CLI will continue executing until it has finished processing all the files. |
| `-w, --overwrite` | False | Flag to overwwrite any existing documentation files. |

### Folder

The `generate folder` command is used to generate documentation for a folder of YAML files. A search pattern can be supplied using `-s, --search` aswell as recursive behaviour using `-c, --recurse`.

```
> embedded-yaml-docs generate folder [OPTIONS]
```

The following options can be supplied for the `generate folder` command.

| Option | Required | Description |
|--------|----------|-------------|
| `-f, --folder` | True | Directory to search for YAML files in. |
| `-t, --template` | True | File path to the Jinja2 template thats used in the documentation generation. |
| `-e, --extension` | False | File type extension to use for the output files that are generated for the documentation. Defaults to `.md`. |
| `-o, --output` | False | Directory to output all the documentation files to. Defaults to the directory supplied by `-f, --folder`. |
| `-s, --search` | False | Wildcard pattern to use when searching for YAML files in the specified folder. Defaults to `*.yml`. |
| `-pre, --exclprefix` | False | List of comment prefixes to search for when generating the documentation. If a prefix is matched, then the corresponding documentation is excluded. To specify multiple prefixes to be excluded repeat the option identifier `-pre, --exclprefix`. |
| `-r, --root` | False | The root folder of your file structure. This is used to calculate relative paths for the YAML files. You could use this to pass your respoitory root meaning that the YAML files, will be relative to the repository. Rather than your file system. |
| `x, --exit` | False | Flag with forces the CLI to stop execution after an error. If this flag is not passed then the CLI will continue executing until it has finished processing all the files. |
| `-c, --recurse` | False | Flag allowing for the search to be executed recursively, against the directory supplied by `-f, --folder`. Otherwise the search will only happen in the top-level folder. |
| `-w, --overwrite` | False | Flag to overwwrite any existing documentation files. |

## Preview

The preview command is used to generate a preview of the documentation data, that will be passed into the Jinja2 template. This allows you to see what information is 'available' and what information can be used in your Jinja2 template.

### File

The `preview folder` command generates the documentation preview for a single file. 

```
> embedded-yaml-docs preview file [OPTIONS]
```

The following options can be supplied for the `generate folder` command.

| Option | Required | Description |
|--------|----------|-------------|
| `-f, --file` | True | File path to the YAML file; to generate the documentation preview for. |
| `-o, --output` | False | File path specifying the location and name of the documentation preview file that will be outputted. If no value is supplied, then the file path supplied using `-f, --file` will be used. Alongwith the extension changed from `.yml` to `.preview`. |
| `-pre, --exclprefix` | False | List of comment prefixes to search for when generating the documentation preview. If a prefix is matched, then the corresponding documentation is excluded. To specify multiple prefixes to be excluded repeat the option identifier `-pre, --exclprefix`. |
| `-r, --root` | False | The root folder of your file structure. This is used to calculate relative paths for the YAML files. You could use this to pass your respoitory root meaning that the YAML files, will be relative to the repository. Rather than your file system. |
| `x, --exit` | False | Flag with forces the CLI to stop execution after an error. If this flag is not passed then the CLI will continue executing until it has finished processing all the files. |
| `-w, --overwrite` | False | Flag to overwwrite any existing documentation preview files. |

### Folder

The `generate folder` command is used to generate documentation previews for a folder of YAML files. A search pattern can be supplied using `-s, --search` aswell as recursive behaviour using `-c, --recurse`.

```
> embedded-yaml-docs preview folder [OPTIONS]
```

The following options can be supplied for the `generate folder` command.

| Option | Required | Description |
|--------|----------|-------------|
| `-f, --folder` | True | Directory to search for YAML files in. |
| `-o, --output` | False | Directory to output all the documentation preview files to. Defaults to the directory supplied by `-f, --folder`. |
| `-s, --search` | False | Wildcard pattern to use when searching for YAML files in the specified folder. Defaults to `*.yml`. |
| `-pre, --exclprefix` | False | List of comment prefixes to search for when generating the documentation. If a prefix is matched, then the corresponding documentation is excluded. To specify multiple prefixes to be excluded repeat the option identifier `-pre, --exclprefix`. |
| `-r, --root` | False | The root folder of your file structure. This is used to calculate relative paths for the YAML files. You could use this to pass your respoitory root meaning that the YAML files, will be relative to the repository. Rather than your file system. |
| `x, --exit` | False | Flag with forces the CLI to stop execution after an error. If this flag is not passed then the CLI will continue executing until it has finished processing all the files. |
| `-c, --recurse` | False | Flag allowing for the search to be executed recursively, against the directory supplied by `-f, --folder`. Otherwise the search will only happen in the top-level folder. |
| `-w, --overwrite` | False | Flag to overwwrite any existing documentation preview files. |

# Dev Notes

- Publishing to pip setup `python -m pip install build twine`, build `python -m build`, check `twine check dist/*`, publish `twine upload dist/*` 
