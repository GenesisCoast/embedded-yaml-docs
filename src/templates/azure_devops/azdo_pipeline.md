<yamldoc>

[&#11013; Back to the <yamldoc eval="_file.name"/> resource](Templates/master/<yamldoc eval="_file.directory"/>)

<br>

[[_TOC_]]

# Introduction

The following page documents the template `/resource/<yamldoc eval="_file.full_name"/>` which is used to deploy the <yamldoc eval="_file.name"/> resource.

# Parameters

Below is a list of the parameters used for the template. Any optional or auto-generated arguments are specified in the schema.

<div style="border:1px solid var(--border-subtle-color);padding:15px 15px 0px 15px">

<span style="color:var(--text-secondary-color)"><strong>Schema:</strong></span>

The template has the following schema. Objects are documented in additional sub-sections below.

```yml
steps:
- template: <yamldoc eval="_file.full_name"/>
  parameters:
    <yamldoc.for exec="for parameter in _parameters">
        <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.type"/> # <yamldoc eval="parameter.description"/>
    </yamldoc.for>
```

---

<div style="color:rgba(0,0,0,.6);margin: 15px 0 16px 0"><strong>Example (with all parameters):</strong></div>

This example shows how to execute the template, with all the possible parameters populated.

```yml
steps:
- template: <yamldoc eval="_file.full_name"/>
  parameters:
    <yamldoc.for exec="for parameter in _parameters" >
        <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.example"/>
    </yamldoc.for>
```

<yamldoc.if
    exec="if 'resourceTags' in _parameters
        or 'resourceTagsString' in _parameters">

<div style="background:#e2daf1;padding:16px 16px 0px 16px;border: 1px solid #e2daf1;color:#000">

<div style="color:#38225d;font-weight:600;font-size: 1.2em">

&#10068;&nbsp;&nbsp;Note

</div>

You should only specify a value for either `resourceTags` or `resourceTagsString`. Do not specify both of the parameters.

</div>

</yamldoc.if>

---

<div style="color:rgba(0,0,0,.6);margin: 15px 0 16px 0"><strong>Example (with only mandatory parameters):</strong></div>

This example shows how to use the template, with only the mandatory parameters specified.

```yml
steps:
- checkout: self
  path: paf

- template: <yamldoc eval="_file.full_name"/>
  parameters:
    <yamldoc.for exec="for parameter in _parameters" >
        <yamldoc.if exec="if parameter.default != ''">
            <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.example"/>
        </yamldoc.if>
    </yamldoc.for>
```

---

<div style="color:rgba(0,0,0,.6);margin: 15px 0 16px 0"><strong>Example (with auto-generation):</strong></div>

This example shows how to use parameters with auto-generation, which allows you to use the bare minimum parameters.

```yml
variables:
  site: mneu
  environment: dev
  role: daaml
  increment: 001

steps:
- checkout: self
  path: paf

- template: <yamldoc eval="_file.full_name"/>
  parameters:
    <yamldoc.for exec="for parameter in _parameters" >
        <yamldoc.if exec="if parameter.default is None">
            <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.example"/>
        </yamldoc.if>
    </yamldoc.for>
```

---

<div style="color:rgba(0,0,0,.6);margin: 15px 0 16px 0"><strong>Example (with framework version):</strong></div>

This example shows how to use parameters with auto-generation, which allows you to use the bare minimum parameters.

```yml
resources:
  repositories:
  - repository: iac
    name: test
    ref: releases/master
    type: git

steps:
- checkout: iac
  path: paf

- template: <yamldoc eval="_file.full_name"/>@iac
  parameters:
    <yamldoc.for exec="for parameter in _parameters" >
        <yamldoc.if exec="if parameter.default != ''">
            <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.example"/>
        </yamldoc.if>
    </yamldoc.for>
```

<yamldoc.if exec="if 'resourceTags' in _parameters">

---

<div style="color:rgba(0,0,0,.6);margin: 15px 0 16px 0"><strong>Example (with resource tags):</strong></div>

This example shows how to specify resource tags for the template.

```yml
steps:
- checkout: self
  path: paf

- template: <yamldoc eval="_file.full_name"/>@iac
  parameters:
    <yamldoc.for exec="for parameter in _parameters" >
        <yamldoc.if exec="if parameter.default != ''">
            <yamldoc eval="parameter.name"/>: <yamldoc eval="parameter.example"/>
        </yamldoc.if>
    </yamldoc.for>
    <yamldoc exp="_parameters['resourceTags'].name">
    <yamldoc exp="_parameters['resourceTags'].example">
```

</yamldoc.if>

<yamldoc.for exec="for parameter in _parameters">

## <yamldoc eval="parameter.name"/>

<yamldoc eval="parameter.description"/>

<div style="border:1px solid var(--border-subtle-color);padding:15px 15px 0px 15px">

<span style="color:var(--text-secondary-color)"><strong>Schema:</strong></span>

The following schema is observed.

```yml
<yamldoc eval="parameter.name"/>:
    <yamldoc.for exec="for property in parameter._properties">
        <yamldoc eval="property.name"/>: <yamldoc eval="property.type"/> # <yamldoc eval="property.description"/>
    </yamldoc.for>
```

---

<div style="color:var(--text-secondary-color);margin: 15px 0 16px 0"><strong>Example:</strong></div>

This example, shows simplified syntax of specifying the <yamldoc eval="parameter.name"/>.

```yml
<yamldoc eval="parameter.name"/>:
    <yamldoc.for exec="for property in parameter._properties">
        <yamldoc eval="property.name"/>: <yamldoc eval="property.example"/>
    </yamldoc.for>
```

</div>

<yamldoc.for>

</yamldoc>