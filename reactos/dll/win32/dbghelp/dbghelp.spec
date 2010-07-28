#
# dbghelp spec file for reactos. Do not replace with wine ones!
#
#@ stub SymGetOmapBlockBase
@ stdcall DbgHelpCreateUserDump(str ptr ptr)
@ stdcall DbgHelpCreateUserDumpW(str ptr ptr)
@ stdcall EnumDirTree(long str str ptr ptr ptr)
@ stdcall EnumDirTreeW(long wstr wstr ptr ptr ptr)
@ stdcall EnumerateLoadedModules64(long ptr ptr)
@ stdcall EnumerateLoadedModules(long ptr ptr)
@ stdcall EnumerateLoadedModulesEx(ptr ptr ptr)
@ stdcall EnumerateLoadedModulesExW(ptr ptr ptr)
@ stdcall EnumerateLoadedModulesW64(long ptr ptr)
@ stdcall ExtensionApiVersion()
@ stdcall FindDebugInfoFile(str str ptr)
@ stdcall FindDebugInfoFileEx(str str ptr ptr ptr)
@ stdcall FindDebugInfoFileExW(str str str ptr ptr)
@ stdcall FindExecutableImage(str str str)
@ stdcall FindExecutableImageEx(str str ptr ptr ptr)
@ stdcall FindExecutableImageExW(wstr wstr ptr ptr ptr)
@ stdcall FindFileInPath(ptr str str ptr long long long str)
@ stdcall FindFileInSearchPath(ptr str str long long long str)
@ stdcall GetTimestampForLoadedLibrary(long)
@ stdcall ImageDirectoryEntryToData(ptr long long ptr)
@ stdcall ImageDirectoryEntryToDataEx(ptr long long ptr ptr)
@ stdcall ImageNtHeader(ptr) ntdll.RtlImageNtHeader
@ stdcall ImageRvaToSection(ptr ptr long) ntdll.RtlImageRvaToSection
@ stdcall ImageRvaToVa(ptr ptr long ptr) ntdll.RtlImageRvaToVa
@ stdcall ImagehlpApiVersion()
@ stdcall ImagehlpApiVersionEx(ptr)
@ stdcall MakeSureDirectoryPathExists(str)
@ stdcall MapDebugInformation(long str str long)
@ stdcall MiniDumpReadDumpStream(ptr long ptr ptr ptr)
@ stdcall MiniDumpWriteDump(ptr long ptr long long long long)
@ stdcall SearchTreeForFile(str str ptr)
@ stdcall SearchTreeForFileW(wstr wstr ptr)
@ stdcall StackWalk64(long long long ptr ptr ptr ptr ptr ptr)
@ stdcall StackWalk(long long long ptr ptr ptr ptr ptr ptr)
@ stdcall SymAddSourceStream(ptr double str ptr ptr)
@ stdcall SymAddSourceStreamA(ptr double str ptr ptr)
@ stdcall SymAddSourceStreamW(ptr double str ptr ptr)
@ stdcall SymAddSymbol(ptr double str double long long)
@ stdcall SymAddSymbolW(ptr double wstr double long long)
@ stdcall SymCleanup(long)
@ stdcall SymDeleteSymbol(ptr double str double long)
@ stdcall SymDeleteSymbolW(ptr double str double long)
@ stdcall SymEnumLines(ptr double str str ptr ptr)
@ stdcall SymEnumLinesW(ptr double str str ptr ptr)
@ stdcall SymEnumProcesses(ptr ptr)
@ stdcall SymEnumSourceFileTokens(ptr double ptr)
@ stdcall SymEnumSourceFiles(ptr double str ptr ptr)
@ stdcall SymEnumSourceFilesW(ptr double str ptr ptr)
@ stdcall SymEnumSourceLines(ptr double str str long long ptr ptr)
@ stdcall SymEnumSourceLinesW(ptr double str str long long ptr ptr)
@ stdcall SymEnumSym(ptr double ptr ptr)
@ stdcall SymEnumSymbols(ptr double str ptr ptr)
@ stdcall SymEnumSymbolsForAddr(ptr double ptr ptr)
@ stdcall SymEnumSymbolsForAddrW(ptr double ptr ptr)
@ stdcall SymEnumSymbolsW(ptr double wstr ptr ptr)
@ stdcall SymEnumTypes(ptr double ptr ptr)
@ stdcall SymEnumTypesByName(ptr double str ptr ptr)
@ stdcall SymEnumTypesByNameW(ptr double str ptr ptr)
@ stdcall SymEnumTypesW(ptr double ptr ptr)
@ stdcall SymEnumerateModules64(long ptr ptr)
@ stdcall SymEnumerateModules(long ptr ptr)
@ stdcall SymEnumerateModulesW64(long ptr ptr)
@ stdcall SymEnumerateSymbols64(long double ptr ptr)
@ stdcall SymEnumerateSymbols(long long ptr ptr)
@ stdcall SymEnumerateSymbolsW64(ptr double ptr ptr)
@ stdcall SymEnumerateSymbolsW(ptr long ptr ptr)
@ stdcall SymFindDebugInfoFile(ptr str str ptr ptr)
@ stdcall SymFindDebugInfoFileW(ptr str str ptr ptr)
@ stdcall SymFindExecutableImage(ptr str str ptr ptr)
@ stdcall SymFindExecutableImageW(ptr str str ptr ptr)
@ stdcall SymFindFileInPath(long str str ptr long long long ptr ptr ptr)
@ stdcall SymFindFileInPathW(long wstr wstr ptr long long long ptr ptr ptr)
@ stdcall SymFromAddr(ptr double ptr ptr)
@ stdcall SymFromAddrW(ptr double ptr ptr)
@ stdcall SymFromIndex(ptr double long ptr)
@ stdcall SymFromIndexW(ptr double long ptr)
@ stdcall SymFromName(long str ptr)
@ stdcall SymFromNameW(long str ptr)
@ stdcall SymFromToken(ptr double long ptr)
@ stdcall SymFromTokenW(ptr double long ptr)
@ stdcall SymFunctionTableAccess64(long double)
@ stdcall SymFunctionTableAccess(long long)
@ stdcall SymGetFileLineOffsets64(ptr str str ptr long)
@ stdcall SymGetHomeDirectory(long str ptr)
@ stdcall SymGetHomeDirectoryW(long str ptr)
@ stdcall SymGetLineFromAddr64(long double ptr ptr)
@ stdcall SymGetLineFromAddr(long long ptr ptr)
@ stdcall SymGetLineFromAddrW64(long double ptr ptr)
@ stdcall SymGetLineFromName64(long str str long ptr ptr)
@ stdcall SymGetLineFromName(long str str long ptr ptr)
@ stdcall SymGetLineFromNameW64(long wstr wstr long ptr ptr)
@ stdcall SymGetLineNext64(long ptr)
@ stdcall SymGetLineNext(long ptr)
@ stdcall SymGetLineNextW64(ptr ptr)
@ stdcall SymGetLinePrev64(long ptr)
@ stdcall SymGetLinePrev(long ptr)
@ stdcall SymGetLinePrevW64(ptr ptr)
@ stdcall SymGetModuleBase64(long double)
@ stdcall SymGetModuleBase(long long)
@ stdcall SymGetModuleInfo64(long double ptr)
@ stdcall SymGetModuleInfo(long long ptr)
@ stdcall SymGetModuleInfoW64(long double ptr)
@ stdcall SymGetModuleInfoW(long long ptr)
@ stub SymGetOmapBlockBase
@ stdcall SymGetOptions()
@ stdcall SymGetScope(ptr double long ptr)
@ stdcall SymGetScopeW(ptr double long ptr)
@ stdcall SymGetSearchPath(long ptr long)
@ stdcall SymGetSearchPathW(long ptr long)
@ stdcall SymGetSourceFile(ptr double str str str long)
@ stdcall SymGetSourceFileFromToken(ptr ptr str str long)
@ stdcall SymGetSourceFileFromTokenW(ptr ptr str str long)
@ stdcall SymGetSourceFileToken(ptr double str ptr ptr)
@ stdcall SymGetSourceFileTokenW(ptr double wstr ptr ptr)
@ stdcall SymGetSourceFileW(ptr double str str str long)
@ stdcall SymGetSourceVarFromToken(ptr ptr str str str long)
@ stdcall SymGetSourceVarFromTokenW(ptr ptr str str str long)
@ stdcall SymGetSymFromAddr64(long double ptr ptr)
@ stdcall SymGetSymFromAddr(long long ptr ptr)
@ stdcall SymGetSymFromName64(long str ptr)
@ stdcall SymGetSymFromName(long str ptr)
@ stdcall SymGetSymNext64(long ptr)
@ stdcall SymGetSymNext(long ptr)
@ stdcall SymGetSymPrev64(long ptr)
@ stdcall SymGetSymPrev(long ptr)
@ stdcall SymGetSymbolFile(ptr str str long str ptr str ptr)
@ stdcall SymGetSymbolFileW(ptr str str long str ptr str ptr)
@ stdcall SymGetTypeFromName(ptr double str ptr)
@ stdcall SymGetTypeFromNameW(ptr double str ptr)
@ stdcall SymGetTypeInfo(ptr double long long ptr)
@ stdcall SymGetTypeInfoEx(ptr double ptr)
@ stdcall SymGetUnwindInfo(ptr double ptr ptr)
@ stdcall SymInitialize(long str long)
@ stdcall SymInitializeW(long wstr long)
@ stdcall SymLoadModule64(long long str str double long)
@ stdcall SymLoadModule(long long str str long long)
@ stdcall SymLoadModuleEx(long long str str double long ptr long)
@ stdcall SymLoadModuleExW(long long wstr wstr double long ptr long)
@ stdcall SymMatchFileName(str str ptr ptr)
@ stdcall SymMatchFileNameW(wstr wstr ptr ptr)
@ stdcall SymMatchString(str str long)
@ stdcall SymMatchStringA(str str long)
@ stdcall SymMatchStringW(str str long)
@ stdcall SymNext(ptr ptr)
@ stdcall SymNextW(ptr ptr)
@ stdcall SymPrev(ptr ptr)
@ stdcall SymPrevW(ptr ptr)
@ stdcall SymRefreshModuleList(long)
@ stdcall SymRegisterCallback64(long ptr double)
@ stdcall SymRegisterCallback(long ptr ptr)
@ stdcall SymRegisterCallbackW64(long ptr double)
@ stdcall SymRegisterFunctionEntryCallback64(ptr ptr double)
@ stdcall SymRegisterFunctionEntryCallback(ptr ptr ptr)
@ stdcall SymSearch(long double long long str double ptr ptr long)
@ stdcall SymSearchW(long double long long wstr double ptr ptr long)
@ stdcall SymSetContext(long ptr ptr)
@ stdcall SymSetHomeDirectory(ptr str)
@ stdcall SymSetHomeDirectoryW(ptr str)
@ stdcall SymSetOptions(long)
@ stdcall SymSetParentWindow(long)
@ stdcall SymSetScopeFromAddr(ptr double)
@ stdcall SymSetScopeFromIndex(ptr double long)
@ stdcall SymSetSearchPath(long str)
@ stdcall SymSetSearchPathW(long wstr)
@ stdcall SymSrvDeltaName(ptr str str str str)
@ stdcall SymSrvDeltaNameW(ptr str str str str)
@ stdcall SymSrvGetFileIndexInfo(str ptr long)
@ stdcall SymSrvGetFileIndexInfoW(str ptr long)
@ stdcall SymSrvGetFileIndexString(ptr str str str ptr long)
@ stdcall SymSrvGetFileIndexStringW(ptr str str str ptr long)
@ stdcall SymSrvGetFileIndexes(str ptr ptr ptr long)
@ stdcall SymSrvGetFileIndexesW(str ptr ptr ptr long)
@ stdcall SymSrvGetSupplement(ptr str str str)
@ stdcall SymSrvGetSupplementW(ptr str str str)
@ stdcall SymSrvIsStore(ptr str)
@ stdcall SymSrvIsStoreW(ptr str)
@ stdcall SymSrvStoreFile(ptr str str long)
@ stdcall SymSrvStoreFileW(ptr str str long)
@ stdcall SymSrvStoreSupplement(ptr str str str long)
@ stdcall SymSrvStoreSupplementW(ptr str str str long)
@ stub SymSetSymWithAddr64
@ stdcall SymUnDName64(ptr str long)
@ stdcall SymUnDName(ptr str long)
@ stdcall SymUnloadModule64(long double)
@ stdcall SymUnloadModule(long long)
@ stdcall UnDecorateSymbolName(str str long long)
@ stdcall UnDecorateSymbolNameW(str str long long)
@ stdcall UnmapDebugInformation(ptr)
@ stdcall WinDbgExtensionDllInit(ptr long long)
#@ stdcall block
#@ stdcall chksym
#@ stdcall dbghelp
#@ stdcall dh
#@ stdcall fptr
#@ stdcall homedir
#@ stdcall itoldyouso
#@ stdcall lmi
#@ stdcall lminfo
#@ stdcall omap
#@ stdcall srcfiles
#@ stdcall stack_force_ebp
#@ stdcall stackdbg
#@ stdcall sym
#@ stdcall symsrv
#@ stdcall vc7fpo
