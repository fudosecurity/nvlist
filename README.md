# FreeBSD's name/value pairs library

[![Build Status](https://travis-ci.org/rmind/nvlist.svg?branch=master)](https://travis-ci.org/rmind/nvlist)

The **libnv** library is a general purpose name/value pairs mechanism used
in FreeBSD, which was inspired by the nvpairs used in Solaris/illumos.
It is a lightweight serialization (marshalling) library.  The implementation
is written in C99 and distributed under the 2-clause BSD license.

The libnv library was implemented by Pawel Jakub Dawidek under sponsorship
from the FreeBSD Foundation.

Upstream: https://github.com/wheelsystems/nvlist/

## Documentation and API

See the FreeBSD's [nv(9) manual page](https://www.freebsd.org/cgi/man.cgi?query=nv&apropos=0&sektion=0&manpath=FreeBSD+11.1-RELEASE&arch=default&format=html).

## Packages

Just build the package, install it and link the library using the `-lnv` flag.
* RPM (tested on RHEL/CentOS 7): `cd pkg && make rpm`
* DEB (tested on Debian 9): `cd pkg && make deb`