Name:		python-pywbem
Version:	1.9.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pywbem/pywbem-%{version}.tar.gz
Summary:	pywbem - A WBEM client
URL:		https://pypi.org/project/pywbem/
License:	LGPL-2.1-or-later
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
pywbem - A WBEM client

%prep -a
rm -rf pywbem.egg-info

%build -p
# The sdist has no git checkout, so setuptools-scm cannot see the tag.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%install -a
# Death to Windows
rm -f %{buildroot}%{_bindir}/*.bat

%files
%{_bindir}/mof_compiler
%{py_sitedir}/pywbem
%{py_sitedir}/pywbem_mock
%{py_sitedir}/pywbem-*.*-info
