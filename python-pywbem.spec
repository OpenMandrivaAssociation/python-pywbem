Name:		python-pywbem
Version:	1.7.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pywbem/pywbem-%{version}.tar.gz
Summary:	pywbem - A WBEM client
URL:		https://pypi.org/project/pywbem/
License:	LGPL version 2.1, or (at your option) any later version
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
pywbem - A WBEM client

%install -a
# Death to Windows
rm %{buildroot}%{_bindir}/*.bat

%files
%{_bindir}/mof_compiler
%{py_sitedir}/pywbem
%{py_sitedir}/pywbem_mock
%{py_sitedir}/pywbem-*.*-info
