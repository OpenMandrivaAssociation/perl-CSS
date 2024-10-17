%define upstream_name    CSS
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Object oriented access to Cascading Style Sheets (CSS) 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Parse::RecDescent)
BuildArch:	noarch

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a CSS::Adaptor::*
module, the CSS data tree can then be transformed into other formats.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README examples
%{perl_vendorlib}/CSS.pm
%{perl_vendorlib}/CSS
%{_mandir}/*/*


%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 648068
- update to new version 1.09

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 403041
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.08-2mdv2009.0
+ Revision: 268390
- rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-3mdv2008.1
+ Revision: 136980
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-2mdv2007.0
- spec cleanup

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.07-1mdk
- initial Mandriva package

