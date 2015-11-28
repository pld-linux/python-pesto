%define 	module	pesto
Summary:	library for Python web applications
Summary(pl.UTF-8):	Biblioteka dla Pythonowych aplikacji sieciowych
Name:		python-%{module}
Version:	25
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	0e00fb8b949f02b86649da4b5efaa2f4
URL:		http://pesto.redgecko.org/index.html
# BuildRequires:	python-distribute
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pesto makes it easy to: Map any URI to any part of your application.
Produce unicode aware, standards compliant WSGI applications.
Interrogate WSGI request information – form variables and HTTP request
headers. Create and manipulate HTTP headers, redirects, cookies etc.

%description -l pl.UTF-8
Pesto mozwala: Mapować URI do fragementów aplikacji. Wygenerować
unicodowe, zgodne ze standardem WSGI aplikacje. Odpytywać informacje
WSGI o zapytaniu w tym zmienne z formatek i nagłówków HTTP. Tworzyć i
manipulować nagłówki HTTP, przekierowania, ciasteczka itp.

%prep
%setup -q -n %{module}-%{version}
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGELOG.txt NEWS.txt README.txt THANKS.txt TODO.txt
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
