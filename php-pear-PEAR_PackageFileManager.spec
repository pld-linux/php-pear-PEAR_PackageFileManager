%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - takes an existing package.xml file and updates it with a new filelist and changelog
Summary(pl):	%{_pearname} - aktualizacja package.xml (dodanie nowej listy plik�w oraz listy zmian)
Name:		php-pear-%{_pearname}
Version:	1.5.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	76b2b2f9c3491e451caf11adebf04df6
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(PHP/CompatInfo.*)' 'pear(XML/Tree.*)'

%description
This package revolutionizes the maintenance of PEAR packages. With a
few parameters, the entire package.xml is automatically updated with a
listing of all files in a package.

Features include:
- reads an existing package.xml file, and only changes the
  release/changelog
- a plugin system for retrieving files in a directory. Currently two
  plugins exist, one for standard recursive directory content listing,
  and one that reads CVS/Entries and generates a file listing based on
  the contents of a checked out CVS repository
- incredibly flexible options for assigning install roles to
  files/directories
- ability to ignore any file based on a * ? wildcard-enabled string
- ability to manage dependencies
- can output the package.xml in any directory, and read in the
  package.xml from any directory
- can specify a different name for the package.xml file

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet rewolucjonizuje zarz�dzanie pakietami PEAR. Za pomoc� kilku
parametr�w mo�liwe jest automatyczne zaktualizowanie package.xml o
list� plik�w danego pakietu.

Mo�liwo�ci pakietu:
- wczytuje istniej�cy plik package.xml i zmienia w nim tylko
  release/changelog
- system wtyczek s�u��cych do skompletowania listy plik�w w katalogu.
  Aktualnie istniej� dwie takie wtyczki - jedna do standardowego
  rekursywnego przegl�dania katalog�w, druga do odczytu do generowania
  listy plik�w na podstawie CVS/Entries.
- niesamowicie elastyczne opcje do okre�lania roli podczas instalacji
  dla plik�w/katalog�w [FIXME?]
- mo�liwo�� ignorowania plik�w na podstawie wildcard�w * ?
- mo�liwo�� do zarz�dzania zale�no�ciami
- mo�liwo�� zapisu pliku package.xml do dowolnego katalogu oraz
  odczytu tego pliku z dowolnego katalogu
- mo�na okre�li� dla pliku package.xml inn� nazw�

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
