%define upstream_name    CSS
%define upstream_version 1.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Object oriented access to Cascading Style Sheets (CSS) 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Parse::RecDescent)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a CSS::Adaptor::*
module, the CSS data tree can then be transformed into other formats.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorlib}/CSS.pm
%{perl_vendorlib}/CSS
%{_mandir}/*/*
