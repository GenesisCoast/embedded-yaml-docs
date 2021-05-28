[![Upload Python Package](https://github.com/GenesisCoast/embedded-yaml-docs/actions/workflows/python-publish.yml/badge.svg)](https://github.com/GenesisCoast/embedded-yaml-docs/actions/workflows/python-publish.yml) [![PyPI version](https://badge.fury.io/py/embedded-yaml-docs.svg)](https://badge.fury.io/py/embedded-yaml-docs)

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

Embedded YAML docs is a CLI for generating documentation about a YAML file, using the comments that have been embedded in the file.

This is incredibly useful for YAML pipelines and configuration files where you may want to automatically generate user readable documentation, depending on the contents of the file.

*azure-pipeline.yml*
```yml
# ---
# Description:
#   This pipeline is used to show an example of how you can print an output to the console.
# ---

parameters:
- name: outputText
  type: string
  # Description:
  #   Text to output to the console.
  # Example:
  #   Hello world.
  
variables:
  System.Debug: true
  # Description:
  #   Variable used to enable all the debug logging for the Azure DevOps pipelines.
  
steps:
- task: Bash@3
  displayName: 'docs: Install the dependencies for "embedded-yaml-docs"'
  # Description:
  #   Installs all the libraries and dependencies required to run the `embedded-yaml-docs` tool.
  inputs:
    script: |
      echo ${{ parameters.outputText }}
    targetType: inline
```
