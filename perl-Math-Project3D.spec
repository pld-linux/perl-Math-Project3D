#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Project3D
Summary:	Math::Project3D - Project functions of multiple parameters from R^3 onto an arbitrary plane
Summary(pl.UTF-8):	Math::Project3D - rzutowanie funkcji wieloparametrowych z R^3 na dowolną powierzchnię
Name:		perl-Math-Project3D
Version:	1.02
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a5f983261f1ecabdfc7985e3cd05a9d
URL:		http://search.cpan.org/dist/Math-Project3D/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Project3D projects functions of multiple parameters from R^3
onto an arbitrary plane.

%description -l pl.UTF-8
Math::Project3D rzutuje funkcje wieloparametrowe z R^3 na dowolną
powierzchnię.

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
%doc Changes README
%{perl_vendorlib}/Math/*.pm
%{perl_vendorlib}/Math/Project3D
%{_mandir}/man3/*
