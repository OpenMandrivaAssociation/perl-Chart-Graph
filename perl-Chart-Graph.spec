%define upstream_name    Chart-Graph
%define upstream_version 3.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl extension for a front-end to gnuplot, XRT, and Xmgrace
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Chart/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Provides:   perl(Base_Option)
Provides:   perl(Chart::Graph::Xmgrace::Axis_Options)
Provides:   perl(Chart::Graph::Xmgrace::Dataset_Options)
Provides:   perl(Chart::Graph::Xmgrace::Graph_Options)

%description 
Graph.pm is a wrapper module that allows easy generation of graphs within perl.
Currently Graph.pm supports three graphing packages, gnuplot, XRT, and Xmgrace.
These software packages must be obtained separately from this Perl module.
Information on each graphing package and it's availability is provided in the
documentation on that module. Gnuplot and Xmgrace are freely available software
pages for UNIX systems. XRT is a commercial product.

Currently the xrt3d and xrt2d package is not being supported, although it
works. It is still in the development stage. Feel free to give it a try though.

The parsers also write the test data into the 'Test Result Publication
Interface' (TRPI) XML schema, developed by SpikeSource.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <</dev/null
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{perl_vendorlib}/Chart
%{_mandir}/*/*
