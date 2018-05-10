# _RPM Development Specs_

A simple repository to host **[RPM](http://rpm.org/)** spec files for various _interesting_ software available on the web.

## **[FiraCode](https://github.com/tonsky/FiraCode)**:

A very nice font with programming ligatures.

- **[spec](firacode-fonts/firacode-fonts.spec)**
- **copr** [**[f28]()**]

#### Installation:

##### Fedora 28

    sudo dnf install firacode-fonts

#### Compilation:

Make sure you have set your RPM development environment up, if not run:

    rpmdev-setuptree

This will create the _~/rpmbuild_ directory with the needed folders.

Once that's done, just run _spectool_ to download the source code and _rpmbuild_ to actually compile the RPM package from the source code.

    spectool -g -R firacode-fonts/firacode-fonts.spec
    rpmbuild -ba firacode-fonts/firacode-fonts.spec

This will produce the following two binary files:

- ~/rpmbuild/SRPMS/firacode-fonts-1.205-2.fc28.src.rpm
- ~/rpmbuild/RPMS/noarch/firacode-fonts-1.205-2.fc28.noarch.rpm

The first one will be the source RPM that contains the source code and the instructions RPM used to build the final binary.

The second one will be the installable (final) binary which writes the software to your machine.
