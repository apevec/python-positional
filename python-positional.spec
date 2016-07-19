%global pypi_name positional

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        4%{?dist}
Summary:        Library to enforce positional or keyword arguments

License:        ASL 2.0
URL:            https://github.com/morganfainberg/positional
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git

%description
A decorator which enforces only some args may be passed positionally.x


%package -n     python2-%{pypi_name}
Summary:        Library to enforce positional or keyword arguments
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-sphinx

%description -n python2-%{pypi_name}
A decorator which enforces only some args may be passed positionally.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Library to enforce positional or keyword arguments
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 1.8
BuildRequires:  python3-sphinx

%description -n python3-%{pypi_name}
A decorator which enforces only some args may be passed positionally.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Python positional documentation
%description -n python-%{pypi_name}-doc
Documentation for positional

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif
# generate html docs
sphinx-build doc/source html
pushd html
iconv -f iso8859-1 -t utf-8 objects.inv > objects.conv && mv -f objects.conv objects.inv
popd
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if 0%{?with_python3}
%py3_install
%endif
%py2_install


%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc html

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.1-2
- Fix minor rpmlint warnings

* Mon Jan 25 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.1-1
- Initial package.
