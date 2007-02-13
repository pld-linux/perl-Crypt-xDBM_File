#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	xDBM_File
Summary:	Crypt::xDBM_File Perl module - encrypt almost any kind of dbm file
Summary(pl.UTF-8):	Moduł Perla Crypt::xDBM_File - szyfrowanie prawie wszystkich rodzajów plików dbm
Name:		perl-Crypt-xDBM_File
Version:	1.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e1c91ebbf896ae094c7b150e4c67883
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-DES
BuildRequires:	perl-Crypt-IDEA
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::xDBM_File encrypts/decrypts the data in a gdbm, ndbm, sdbm (and
maybe even BerkeleyDB, but it wasn't tested by the author) file. It
gets tied to a hash and you just access the hash like normal. The
crypt function can be any of the CPAN modules that use encrypt,
decrypt, keysize, blocksize (so Crypt::IDEA, Crypt::DES,
Crypt::Blowfish... should all work).

%description -l pl.UTF-8
Moduł Crypt::xDBM_File szyfruje i deszyfruje dane w plikach gdbm,
ndbm, sdbm (być może także BerkeleyDB, ale nie było to testowane przez
autora). Moduł przywiązuje się do hasza, do którego można potem
odwoływać się w normalny sposób. Funkcją szyfrująca może być dowolny z
modułów CPAN używający funkcji encrypt, decrypt, keysize, blocksize
(czyli moduły Crypt::IDEA, Crypt::DES, Crypt::Blowfish... powinny
wszystkie działać).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/xDBM_File.pm
%{_mandir}/man3/*
