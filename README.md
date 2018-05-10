# _RPM Development Specs_

A simple repository to host **[RPM](http://rpm.org/)** spec files for various _interesting_ software available on the web.

It provides instructions for **compiling**, **installing** and **deploying** each supported package to places like [COPR](https://copr.fedorainfracloud.org) and [OBS](https://build.opensuse.org).

|Packages||
|---|---|
|**[FiraCode](#firacode)**|<a href="https://copr.fedorainfracloud.org/coprs/galaticstryder/firacode-fonts/package/firacode-fonts"><img src="https://copr.fedorainfracloud.org/coprs/galaticstryder/firacode-fonts/package/firacode-fonts/status_image/last_build.png"/></a>|

## General Compilation

#### Fedora:

Make sure you have set your RPM development environment up, if not, run:

    rpmdev-setuptree

This will create the _~/rpmbuild_ directory with the needed folders.

Once that's done, just run _spectool_ to download the source code and _rpmbuild_ to actually compile the RPM package from the source code.

    # Replace $package with the target package name.
    spectool -g -R $package/$package.spec
    rpmbuild -ba $package/$package.spec

This will download the _Source0_ pointed in the spec file and then build the RPM and SRPM.

They'll be located at:

- ~/rpmbuild/SRPMS
- ~/rpmbuild/RPMS

The first directory will contain the source RPM that contains the source code and the instructions _rpmbuild_ used to build the final RPM binary.

The second directory will contain the installable (final) RPM binary which writes the software to your machine.

## **[FiraCode](https://github.com/tonsky/FiraCode)**:

#### firacode-fonts

A very nice font with programming ligatures.

- **[spec](firacode-fonts/firacode-fonts.spec)**
- **[copr](https://copr.fedorainfracloud.org/coprs/galaticstryder/firacode-fonts)** [**f28**, **rawhide**]

#### Installation:

##### Fedora 28/Rawhide

    sudo dnf copr enable galaticstryder/firacode-fonts
    sudo dnf install firacode-fonts

#### Compilation:

Refer to [General Compilation](#general-compilation) above.
