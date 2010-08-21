%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - takes an existing package.xml file and updates it with a new filelist and changelog
Summary(pl.UTF-8):	%{_pearname} - aktualizacja package.xml (dodanie nowej listy plików oraz listy zmian)
Name:		php-pear-%{_pearname}
Version:	1.7.0
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	07d1f5f6256b8e97c5910b7908b9282e
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.1
Requires:	php-pear-PEAR_PackageFileManager2
Requires:	php-pear-PEAR_PackageFileManager_Plugins
Suggests:	php-pear-PHP_CompatInfo
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

%description -l pl.UTF-8
Ten pakiet rewolucjonizuje zarządzanie pakietami PEAR. Za pomocą kilku
parametrów możliwe jest automatyczne zaktualizowanie package.xml o
listę plików danego pakietu.

Możliwości pakietu:
- wczytuje istniejący plik package.xml i zmienia w nim tylko
  release/changelog
- system wtyczek służących do skompletowania listy plików w katalogu.
  Aktualnie istnieją dwie takie wtyczki - jedna do standardowego
  rekursywnego przeglądania katalogów, druga do odczytu do generowania
  listy plików na podstawie CVS/Entries.
- niesamowicie elastyczne opcje do określania roli podczas instalacji
  dla plików/katalogów [FIXME?]
- możliwość ignorowania plików na podstawie wildcardów * ?
- możliwość do zarządzania zależnościami
- możliwość zapisu pliku package.xml do dowolnego katalogu oraz
  odczytu tego pliku z dowolnego katalogu
- można określić dla pliku package.xml inną nazwę

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
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
