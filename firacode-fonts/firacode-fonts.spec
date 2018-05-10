%global fontname firacode

Name:           %{fontname}-fonts
Version:        1.205
Release:        2%{?dist}
Summary:        Mono-spaced font with programming ligatures

License:        OFL
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/archive/1.205.tar.gz

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       fontpackages-filesystem

%description
Fira Code is an extension of the Fira Mono font containing a set of ligatures
for common programming multi-character combinations.

%prep
%autosetup -n FiraCode-%{version}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p distr/ttf/*.ttf %{buildroot}%{_fontdir}

%files
%license LICENSE
%doc README.md
%{_fontdir}/*.ttf

%changelog
* Thu May 10 2018 Ícaro Pereira Hoff <icarohoff@gmail.com> - 1.205-2
- changed package name to firacode-fonts

* Wed May 09 2018 Ícaro Pereira Hoff <icarohoff@gmail.com> - 1.205-1
- created specfile
