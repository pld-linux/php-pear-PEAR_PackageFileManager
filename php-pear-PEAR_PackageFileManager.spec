%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - takes an existing package.xml file and updates it with a new filelist and changelog
Summary(pl):	%{_pearname} - aktualizacja package.xml (dodanie nowej listy plików oraz listy zmian)
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fd102343fd7a70750008af4a271a1466
URL:		http://pear.php.net/package/PEAR_PackageFileManager/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Ten pakiet rewolucjonizuje zarz±dzanie pakietami PEAR. Za pomoc± kilku
parametrów mo¿liwe jest automatyczne zaktualizowanie package.xml o
listê plików danego pakietu.

Mo¿liwo¶ci pakietu:
- wczytuje istniej±cy plik package.xml i zmienia w nim tylko
  release/changelog
- system wtyczek s³u¿±cych do skompletowania listy plików w katalogu.
  Aktualnie istniej± dwie takie wtyczki - jedna do standardowego
  rekursywnego przegl±dania katalogów, druga do odczytu do generowania
  listy plików na podstawie CVS/Entries.
- niesamowicie elastyczne opcje do okre¶lania roli podczas instalacji
  dla plików/katalogów [FIXME?]
- mo¿liwo¶æ ignorowania plików na podstawie wildcardów * ?
- mo¿liwo¶æ do zarz±dzania zale¿no¶ciami
- mo¿liwo¶æ zapisu pliku package.xml do dowolnego katalogu oraz
  odczytu tego pliku z dowolnego katalogu
- mo¿na okre¶liæ dla pliku package.xml inn± nazwê

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,tests}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
