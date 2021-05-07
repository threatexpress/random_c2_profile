"""
Variables are mapped to the variable in c2profile_template.jinja template
"""

from core.functions import *

variables = {
# Created
"timestamp"                     : get_date(),
# Timing
"sleeptime"                     : get_sleeptime(),
"jitter"                        : get_jitter(),
"data_jitter"                   : get_datajitter(),
# HTTP Client Header Removal
"headers_remove"                : "Strict-Transport-Security",
# User-Agent
"useragent"                     : get_useragent(),
# SSL Certificate
"https_certificate_C"           : get_https_certificate_c(),
"https_certificate_CN"          : get_https_certificate_cn(),
"https_certificate_O"           : get_https_certificate_o(),
"https_certificate_OU"          : get_https_certificate_ou(),
"https_certificate_V"           : "365",
# TCP Beacon
"tcp_port"                      : get_tcpport(),
"tcp_frame_header"              : get_tcp_frame_header(),
# SMB Beacon
"smb_pipename"                  : get_pipename(),
"smb_pipename_stager"           : get_pipename(),
"smb_frame_header"              : get_smb_frame_header(),
# DNS Options
"dns_beacon_dns_idle"           : get_dns_dnsidle(),
"dns_beacon_dns_max_txt"        : "252",
"dns_beacon_dns_sleep"          : get_dns_sleep(),
"dns_beacon_dns_ttl"            : get_dns_ttl(),
"dns_beacon_maxdns"             : get_dns_maxdns(),
"dns_beacon_dns_stager_prepend" : get_dns_host(),
"dns_beacon_dns_stager_subhost" : get_dns_host(),
"dns_beacon_beacon"             : get_dns_host(),
"dns_beacon_get_A"              : get_dns_host(),
"dns_beacon_get_AAAA"           : get_dns_host(),
"dns_beacon_get_TXT"            : get_dns_host(),
"dns_beacon_put_metadata"       : get_dns_host(),
"dns_beacon_put_output"         : get_dns_host(),
"dns_beacon_ns_response"        : "zero",
# SSH Beacon
"ssh_banner"                    : get_ssh_banner(),
"ssh_pipename"                  : get_pipename(),
# Staging
"host_stage"                    : "true", # Staging on or off
# Staging - Server Settings
"http_stager_uri_x86"           : get_random_uri(),
"http_stager_uri_x64"           : get_random_uri(),
"http_stager_server_header1"    : get_http_server_headers(), # Header: Server
"http_stager_server_header2"    : '"Cache-Control" "max-age=0, no-cache"',
"http_stager_server_header3"    : '"Pragma" "no-cache"',
"http_stager_server_header4"    : '"Connection" "keep-alive"',
"http_stager_server_header5"    : get_http_server_contenttype(), # Header: Content-Type
"http_stager_server_prepend"    : get_http_content(),
"http_stager_server_append"     : get_http_content(),

# Staging - Client Settings
"http_stager_client_header1"    : get_http_client_accept(), # Header: Accept
"http_stager_client_header2"    : get_http_client_accept_language(), # Header: Accept-Language
"http_stager_client_header3"    : get_http_client_accept_encoding(), # Header: Accept-Encoding
# Post Exploitation
"post_ex_spawnto_x86"           : get_post_ex_spawnto_x86(),
"post_ex_spawnto_x64"           : get_post_ex_spawnto_x64(),
"post_ex_obfuscate"             : "true",
"post_ex_smartinject"           : "true",
"post_ex_amsi_disable"          : "true",
"post_ex_pipename"              : get_post_ex_pipename_list(),
"post_ex_keylogger"             : "GetAsyncKeyState", # options are GetAsyncKeyState (default) or SetWindowsHookEx
# Memory Indicators
"allocator_settings"            : get_stage_allocator(), # Options: HeapAlloc, MapViewOfFile, or VirtualAlloc
"stage_magic_mz_x86"            : "MZREMZRE", # Override the first bytes (MZ header included) of Beacon's Reflective DLL. Valid x86 instructions are required. Follow instructions that change CPU state with instructions that undo the change.
"stage_magic_mz_x64"            : "MZARMZAR", # Override the first bytes (MZ header included) of Beacon's Reflective DLL. Valid x86 instructions are required. Follow instructions that change CPU state with instructions that undo the change.
"stage_magic_pe"                : get_stage_magic_pe(),
#"stage_userwx"                  : "false",
"stage_stomppe"                 : "true",
"stage_obfuscate"               : "true",
"stage_cleanup"                 : "true",
"stage_sleep_mask"              : "true",
"stage_smartinject"             : "true",
"stage_checksum"                : "0",
"stage_compile_time"            : get_stage_compile_time(),
"stage_entry_point"             : get_stage_entry_point(),
"stage_image_size_x86"          : get_stage_image_size_x86(),
"stage_image_size_x64"          : get_stage_image_size_x64(),
"stage_name"                    : get_stage_name(),
"stage_rich_header"             : get_stage_rich_header(),
"stage_module_x64"              : "netshell.dll",
"stage_module_x86"              : "netshell.dll",
"stage_transform_x86_prepend"   : get_nops(),
"stage_transform_x86_strrep1"   : get_random_object(),
"stage_transform_x64_prepend"   : get_nops(),
"stage_transform_x64_strrep1"   : get_random_object(),
# Process Injection
"process_inject_allocator"      : get_process_inject_allocator(),
"process_inject_min_alloc"      : get_process_inject_min_alloc(),
"process_inject_startrwx"       : "false",
"process_inject_userwx"         : "false",
"process_inject_transform_x86_prepend" : get_nops(),
"process_inject_transform_x86_append"  : get_nops(),
"process_inject_transform_x64_prepend" : get_nops(),
"process_inject_transform_x64_append"  : get_nops(),
"process_inject_execute"               : get_process_inject_execute(),
# HTTP Headers
"http_config_headers"                  : "Date, Server, Content-Length, Keep-Alive, Connection, Content-Type",
"http_config_header_server"            : get_http_config_headers(),
"http_config_trust_x_forwarded_for"    : "true",
"http_config_block_useragents"         : "curl*,lynx*,wget*",
# HTTP GET
"http_get_uri"                         : get_random_uri(),
"http_get_verb"                        : "GET",
"http_get_client_header1"              : get_http_client_accept(),
"http_get_client_header2"              : get_http_client_accept_language(),
"http_get_client_header3"              : get_http_client_accept_encoding(),
"http_get_client_metadata_transform"   : get_http_metadata_transform(),
"http_get_client_metadata_prepend"     : get_http_client_metadata_cookie(),
"http_get_server_header1"              : get_http_server_headers(), # Header: Server
"http_get_server_header2"              : '"Cache-Control" "max-age=0, no-cache"',
"http_get_server_header3"              : '"Pragma" "no-cache"',
"http_get_server_header4"              : '"Connection" "keep-alive"',
"http_get_server_header5"              : get_http_server_contenttype(), # Header: Content-Type
"http_get_server_transform"            : get_http_metadata_transform(),
"http_get_server_prepend"              : get_http_content(),
"http_get_server_append"               : get_http_content(),
# HTTP POST
"http_post_uri"                        : get_random_uri(),
"http_post_verb"                       : "POST",
"http_post_client_header1"             : get_http_client_accept(),
"http_post_client_header2"             : get_http_client_accept_language(),
"http_post_client_header3"             : get_http_client_accept_encoding(),
"http_post_client_id_transform"        : get_http_metadata_transform(),
"http_post_client_id_parameter"        : get_http_post_client_id_parameter(),
"http_post_client_output_transform"    : get_http_metadata_transform(),
"http_post_server_header1"             : get_http_server_headers(), # Header: Server
"http_post_server_header2"             : '"Cache-Control" "max-age=0, no-cache"',
"http_post_server_header3"             : '"Pragma" "no-cache"',
"http_post_server_header4"             : '"Connection" "keep-alive"',
"http_post_server_header5"             : get_http_server_contenttype(), # Header: Content-Type
"http_post_server_transform"           : get_http_metadata_transform(),
"http_post_server_prepend"             : get_http_content(),
"http_post_server_append"              : get_http_content(),

}
