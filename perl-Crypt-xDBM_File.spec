#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	xDBM_File
Summary:	Crypt::xDBM_File Perl module - encrypt almost any kind of dbm file
Summary(pl):	Modu³ Perla Crypt::xDBM_File - szyfrowanie prawie wszystkich rodzajów plików dbm
Name:		perl-Crypt-xDBM_File
Version:	0.80
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c07a00db6ac16c3f93f95767b055645
Patch0:		%{name}-DES.patch
BuildRequires:	perl-devel >= 5.6
%{!?_without_tests:BuildRequires:	perl-Crypt-Blowfish}
%{!?_without_tests:BuildRequires:	perl-Crypt-DES}
%{!?_without_tests:BuildRequires:	perl-Crypt-IDEA}
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

%description -l pl
Modu³ Crypt::xDBM_File szyfruje i deszyfruje dane w plikach gdbm,
ndbm, sdbm (byæ mo¿e tak¿e BerkeleyDB, ale nie by³o to testowane przez
autora). Modu³ przywi±zuje siê do hasza, do którego mo¿na potem
odwo³ywaæ siê w normalny sposób. Funkcj± szyfruj±ca mo¿e byæ dowolny z
modu³ów CPAN u¿ywaj±cy funkcji encrypt, decrypt, keysize, blocksize
(czyli modu³y Crypt::IDEA, Crypt::DES, Crypt::Blowfish... powinny
wszystkie dzia³aæ).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

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
