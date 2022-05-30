
<!-- These markdown files are supposed to be read by doxygen, 
a software for generating documentation. So don't wonder about the @tableofcontents, 
@note and <h1> statements. Please refer as well to the 
official documentation at developer.ubirch.com -->

## Python Implementation 

<h1> Getting Started </h1>

Take a look at the [Quickstart](@ref quickstart) or at the more detailed [Step by Step guide](@ref stepByStep).

Afterwards consider the Article about a [UPP's Lifecycle](@ref uppLifecycle)

---

<h1> Components </h1>

The ubirch library consists of three parts which can be used individually:

**[API](@ref ubirch.ubirch_api.API)** - `ubirch.ubirch_api.API` 

- A python layer covering the ubirch backend REST API

**[Protocol](@ref ubirch.ubirch_protocol.Protocol)** - `ubirch.ubirch_protocol.Protocol`

- The protocol compiler which packages messages and handles signing and verification

**[KeyStore](@ref ubirch.ubirch_ks.KeyStore)** - `ubirch.ubirch_ks.KeyStore`

- A simple key store based on [pyjks](https://pypi.org/project/pyjks/) to store keys and certificates

> The [ubirch](https://ubirch.com) protocol uses the [Ed25519](https://ed25519.cr.yp.to/) signature scheme by default. But [ECDSA](https://www.encryptionconsulting.com/education-center/what-is-ecdsa/) is implemented as well.

@note There is darkmode! You can find it in the upper right corner.
