%define module  CSS
%define name    perl-%{module}
%define version 1.08
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Object oriented access to Cascading Style Sheets (CSS) 
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Parse::RecDescent)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a CSS::Adaptor::*
module, the CSS data tree can then be transformed into other formats.

%prep
%setup -q -n %{module}-%{version} 

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


