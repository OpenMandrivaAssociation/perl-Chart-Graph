%define upstream_name    Chart-Graph
%define upstream_version 3.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for a front-end to gnuplot, XRT, and Xmgrace
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Chart/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

Provides:	perl(Base_Option)
Provides:	perl(Chart::Graph::Xmgrace::Axis_Options)
Provides:	perl(Chart::Graph::Xmgrace::Dataset_Options)
Provides:	perl(Chart::Graph::Xmgrace::Graph_Options)

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
perl Makefile.PL INSTALLDIRS=vendor <</dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%doc COPYING ChangeLog README
%{perl_vendorlib}/Chart
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 3.200.0-2mdv2011.0
+ Revision: 680774
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.200.0-1mdv2011.0
+ Revision: 505423
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.2-8mdv2010.0
+ Revision: 430323
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.2-7mdv2009.0
+ Revision: 256404
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.2-5mdv2008.1
+ Revision: 136680
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-5mdv2008.0
+ Revision: 31160
- fix dependencies


* Fri Mar 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-4mdv2007.1
+ Revision: 148530
- fix dependencies (again)

* Tue Mar 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-3mdv2007.1
+ Revision: 147040
- fix dependencies

* Tue Mar 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-2mdv2007.1
+ Revision: 147038
- this is a noarch package

* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-1mdv2007.1
+ Revision: 143468
- Imported perl-Chart-Graph-3.2-1mdv2007.1 into SVN repository.

* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-1mdv2007.1
- first mdv release

