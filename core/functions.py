import datetime
import random
import string
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, SoftwareType, Popularity

###################
# Helper Functions and Variables

# Create list from object-wordlist
objects = []
with open("core/object-wordlist.txt", "r") as f:
    objects = f.read().split()

# Create list from object-wordlist
actions = []
with open("core/action-wordlist.txt", "r") as f:
    actions = f.read().split()

def get_date():
    """ Formatted Date/Time String """

    date = datetime.datetime.now()	
    dateStr = date.strftime("%Y%m%d_%H%M")
    return dateStr

def get_random_string(length):
    # Return random string of uppercase characters of provided length
    # choose from all uppercase letter
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_alphanum(length):
    # Return random string of uppercase/digits characters of provided length
    alphanum = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(alphanum) for i in range(length))
    return str(result_str)

def get_random_object():
    # Return random object from list
    return random.choice(objects)

def get_random_action():
    # Return random action from list
    return random.choice(actions)

def get_random_uri():
    # Return random URI as /<random action>/<random object>?<random 2 char>=<random alphanum>
    result = "/" + get_random_action() + "/" + get_random_object() + "/" + get_random_alphanum(random.randint(8,12))
    return result

def get_random_bytearry(length):
    # Return random bytearray as \x formatted strng
    # example: \x74\x90\xc9\xf2
    # hex value range
    low = 80
    high = 255
    result = ""
    for i in range(length):
        h = random.randint(low,high)
        hh = bytearray([h]).hex()
        result += '\\x' + hh
    return str(result)

def get_http_client_accept():
    # Return Random HTTP Header Accept from list
    accepts = ['text/html', 'application/xhtml+xml', 'application/xml', 'image/*', 'application/json']
    picks = random.sample(accepts,3)
    accept = '"Accept" "' + picks[0] + ", " + picks[1] + ", " + picks[2] + '"'
    return accept

def get_http_client_accept_language():
    # Return Random HTTP Header Accept-Language from list
    languages = ["af", "sq", "ar-dz", "ar-bh", "ar-eg", "ar-iq", "ar-jo", "ar-kw", "ar-lb", "ar-ly", "ar-ma", "ar-om", "ar-qa", "ar-sa", "ar-sy", "ar-tn", "ar-ae", "ar-ye", "eu", "be", "bg", "ca", "zh-hk", "zh-cn", "zh-sg", "zh-tw", "hr", "cs", "da", "nl-be", "nl", "en", "en-au", "en-bz", "en-ca", "en-ie", "en-jm", "en-nz", "en-za", "en-tt", "en-gb", "en-us", "et", "fo", "fa", "fi", "fr-be", "fr-ca", "fr-lu", "fr", "fr-ch", "gd", "de-at", "de-li", "de-lu", "de", "de-ch", "el", "he", "hi", "hu", "is", "id", "ga", "it", "it-ch", "ja", "ko", "ko", "ku", "lv", "lt", "mk", "ml", "ms", "mt", "no", "nb", "nn", "pl", "pt-br", "pt", "pa", "rm", "ro", "ro-md", "ru", "ru-md", "sr", "sk", "sl", "sb", "es-ar", "es-bo", "es-cl", "es-co", "es-cr", "es-do", "es-ec", "es-sv", "es-gt", "es-hn", "es-mx", "es-ni", "es-pa", "es-py", "es-pe", "es-pr", "es", "es-uy", "es-ve", "sv", "sv-fi", "th", "ts", "tn", "tr", "uk", "ur", "ve", "vi", "cy", "xh", "ji", "zu"]
    language = '"Accept-Language" "' + random.choice(languages) + '"'
    return language

def get_http_client_accept_encoding():
    # Return Random HTTP Header Accept-Encoding from list
    accept_encodings = ['gzip', 'br', 'identity', '*','compress']
    picks = random.sample(accept_encodings, 2)
    accept_encoding = '"Accept-Encoding" "' + picks[0] + ", " + picks[1] + '"'
    return accept_encoding   

def get_http_metadata_transform():
    # Return random Data Transform Language (https://www.cobaltstrike.com/help-malleable-c2)
    transformations = ['base64url','netbios','netbiosu']
    return random.choice(transformations)

def get_http_content():
    # Return random blog of HTTP response content
    contents = [
    ##Start jquery v3.4.1##
    "/*! jQuery v3.4.1 | (c) JS Foundation and other contributors | jquery.org/license */\
    !function(e,t){\'use strict\';\'object\'==typeof module&&\'object\'==typeof module.exports?\
    module.exports=e.document?t(e,!0):function(e){if(!e.document)throw new Error(\'jQuery \
    requires a window with a document\');return t(e)}:t(e)}(\'undefined\'!=typeof window?window\
    :this,function(C,e){\'use strict\';var t=[],E=C.document,r=Object.getPrototypeOf,s=t.slice\
    ,g=t.concat,u=t.push,i=t.indexOf,n={},o=n.toString,v=n.hasOwnProperty,a=v.toString,l=\
    a.call(Object),y={},m=function(e){return\'function\'==typeof e&&\'number\'!=typeof e.nodeType}\
    ,x=function(e){return null!=e&&e===e.window},c={type:!0,src:!0,nonce:!0,noModule:!0};fun\
    ction b(e,t,n){var r,i,o=(n=n||E).createElement(\'script\');if(o.text=e,t)for(r in c)(i=t[\
    r]||t.getAttribute&&t.getAttribute(r))&&o.setAttribute(r,i);n.head.appendChild(o).parentNode;"
    ##End jquery v3.4.1##
    ,
    ##Start jquery ui v1.12.1##
    "/*! jQuery UI - v1.12.1 - 2016-09-14\
    * http://jqueryui.com\
    * Includes: widget.js, position.js,\
    data.js, disable-selection.js, effect.js, effects/effect-blind.js, effects/effect-bounce.js\
    , effects/effect-clip.js, effects/effect-drop.js, effects/effect-explode.js, effects/effect\
    -fade.js, effects/effect-fold.js, effects/effect-highlight.js, effects/effect-puff.js, effe\
    cts/effect-pulsate.js, effects/effect-scale.js, effects/effect-shake.js, effects/effect-s\
    ize.js, effects/effect-slide.js, effects/effect-transfer.js, focusable.js, form-reset-mix\
    in.js, jquery-1-7.js, keycode.js, labels.js, scroll-parent.js, tabbable.js, unique-id.js,\
    widgets/accordion.js, widgets/autocomplete.js, widgets/button.js, widgets/checkboxradio.\
    js, widgets/controlgroup.js, widgets/datepicker.js, widgets/dialog.js, widgets/draggable\
    .js, widgets/droppable.js, widgets/menu.js, widgets/mouse.js, widgets/progressbar.js, w\
    idgets/resizable.js, widgets/selectable.js, widgets/selectmenu.js, widgets/slider.js, w\
    idgets/sortable.js, widgets/spinner.js, widgets/tabs.js, widgets/tooltip.js\
    * Copyright jQuery Foundation and other contributors; Licensed MIT */"
    ##End jquery ui v1.12.1##
    ,
    ##Start jquery v2.2.4##
    "/*! jQuery v2.2.4 | (c) jQuery Foundation | jquery.org/license */\
    !function(a,b){\'object\'==typeof module&&\'object\'==typeof module.exp\
    orts?module.exports=a.document?b(a,!0):function(a){if(!a.document)th\
    row new Error(\'jQuery requires a window with a document\');return b(a\
    )}:b(a)}(\'undefined\'!=typeof window?window:this,function(a,b){var c=\
    [],d=a.document,e=c.slice,f=c.concat,g=c.push,h=c.indexOf,i={},j=i.t\
    oString,k=i.hasOwnProperty,l={},m=\'2.2.4\',n=function(a,b){return new \
    n.fn.init(a,b)},o=/^[suFEFFxA0]+|[suFEFFxA0]+$/g,p=/^-ms-/,q=/-\
    ([da-z])/gi,r=function(a,b){return b.toUpperCase()};n.fn=n.prototype\
    ={jquery:m,constructor:n,selector:\'\',length:0,toArray:function(){retu\
    rn e.call(this)},get:function(a){return null!=a?0>a?this[a+this.lengt\
    h]:this[a]:e.call(this)},pushStack:function(a){var b=n.merge(this.con\
    structor(),a);return b.prevObject=this,b.context=this.context,b},each:"
    ##End jquery v2.2.4##
    ] 
    return random.choice(contents)

def get_nops():
    # Return random bytearry of NOP equvilants as \x formatted string
    # short list of nop equivilants

    # | LENGTH  |           ASSEMBLY                       |         BYTE SEQUENCE        |
    # |---------|------------------------------------------|------------------------------|
    # |         |                                          |                              |
    # | 2 bytes |  66 NOP                                  |  66 90H                      |
    # | 3 bytes |  NOP DWORD ptr [EAX]                     |  0F 1F 00H                   |
    # | 4 bytes |  NOP DWORD ptr [EAX + 00H]               |  0F 1F 40 00H                |
    # | 5 bytes |  NOP DWORD ptr [EAX + EAX*1 + 00H        |  0F 1F 44 00 00H             |
    # | 6 bytes |  66 NOP DWORD ptr [EAX + EAX*1 + 00H     |  66 0F 1F 44 00 00H          |
    # | 7 bytes |  NOP DWORD ptr [EAX + 00000000 H         |  0F 1F 80 00 00 00 00H       |
    # | 8 bytes |  NOP DWORD ptr [EAX + EAX*1 + 00000000H  |  0F 1F 84 00 00 00 00 00H    |
    # | 9 bytes |  66 NOP DWORD ptr [EAX + EAX*1 00000000H |  66 0F 1F 84 00 00 00 00 00H |

    nops = [
        ['90'],                                        # nop
        ['50','58'],                                   # push eax; pop eax
        ['66','90'],                                   # 2 bytes, 0x66; NOP *
        ['0f','1f','00'],                              # 3 bytes, NOP DWORD ptr [EAX]
        ['0f','1f','40','00'],                         # 4 bytes, NOP DWORD ptr [EAX + 00H]
        ['0f','1f','44','00','00'],                    # 5 bytes, 66 NOP DWORD ptr [EAX + EAX*1 + 00H 
        ['66','0f','1f','44','00','00'],               # 6 bytes, NOP DWORD ptr [EAX + EAX*1 + 00H
        ['0f','1f','80','00','00','00','00'],          # 7 bytes, NOP DWORD ptr [EAX + EAX*1 + 00000000H 
        ['0f','1f','84','00','00','00','00','00'],     # 8 bytes, NOP DWORD ptr [EAX + EAX*1 + 00000000H
        ['66','0f','1f','84','00','00','00','00','00'] # 9 bytes, 66 NOP DWORD ptr [EAX + EAX*1 00000000H
    ]

    length = random.randint(5,20)
    nopsled = ""

    for i in range(length):
        nopsled += "\\x" + "\\x".join(random.choice(nops))
    return(nopsled)


###################
# Profile Functions
def get_sleeptime():
    # Return random sleep in milliseconds
    low = 60 * 1000 # 1 minute
    high = 120 * 1000 # 2 minute
    return str(random.randint(low,high))

def get_jitter():
    # Return random jitter
    low = 33
    high = 49
    return str(random.randint(low,high))

def get_datajitter():
    # Return random data jitter
    low = 100
    high = 300
    return str(random.randint(low,high))

def get_useragent():
    # Return random User-Agent string from the random_user_agent module
    # Set Filter Parameters
    software_names    = [SoftwareName.CHROME.value, SoftwareName.CHROMIUM.value, SoftwareName.EDGE.value, SoftwareName.FIREFOX.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]   
    hardware_type     = [HardwareType.COMPUTER.value]
    software_type     = [SoftwareType.WEB_BROWSER.value]
    popularity        = [Popularity.POPULAR.value, Popularity.COMMON.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, hardware_type=hardware_type, software_type=software_type, popularity=popularity, limit=500)
    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent

def get_https_certificate_c():
    # Certificate C value
    c = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR",
    "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE",
    "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO",
    "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD",
    "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI",
    "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG",
    "SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF",
    "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD",
    "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN",
    "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT",
    "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG",
    "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK",
    "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT",
    "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA",
    "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP",
    "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN",
    "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN",
    "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC",
    "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES",
    "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ",
    "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV",
    "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN",
    "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]

    return random.choice(c)

def get_https_certificate_cn():
    # Certificate CN value
    return get_random_object() + random.choice([".net",".com",".org"])

def get_https_certificate_o():
    # Certificate O value
    return get_random_object()

def get_https_certificate_ou():
    # Certificate OU value
    return get_random_object() + " " + random.choice(["sales", "operations", "legal", "IT","corp"])

def get_tcpport():
    # randdom tcp_port between 1024-60000 (excludes 4000's)
    return str(random.choice((list(range(1024,3999))+list(range(5000,60000)))))

def get_tcp_frame_header():
    # Value to Prepend header to TCP Beacon messages
    length = random.randint(5,35)
    result = get_random_bytearry(length)
    return result

def get_pipename():
    # Name of pipe. Each # is replaced with a random hex value.
    names =  ['ProtectionManager_' + get_random_string(4) + '_##', 'Winsock2\\\\CatalogChangeListener-' + get_random_string(4) + '###-1', 'Spool\\\\pipe_' + get_random_string(4) + '_##', 'WkSvcPipeMgr_' + get_random_string(4) + '##', 'NetClient_' + get_random_string(4) + '##', 'RPC_' + get_random_string(4) + '##','WiFiNetMgr' + get_random_string(4) + '_##','AuthPipe' + get_random_string(4) + '_##']
    return random.choice(names)

def get_smb_frame_header():
    # Prepend header to SMB Beacon messages
    length = random.randint(5,35)
    result = get_random_bytearry(length)
    return result

def get_dns_dnsidle():
    # dns_idle any valid IP address not starting with 0, 10, 172, 192 or 255
    ip_num = list(range(1,9)) + list(range(11,171)) + list(range(173,191)) + list(range(193,254))
    dns_idle = ".".join(map(str, (random.choice(ip_num) for _ in range(4))))   
    return dns_idle

def get_dns_maxtxt():
    #Maximum length of DNS TXT responses for tasks
    return str(random.randint(240,254))

def get_dns_sleep():
    # Force a sleep prior to each individual DNS request. (in milliseconds)
    return str(random.randint(240,254))

def get_dns_ttl():
    # TTL for DNS replies
    return str(random.randint(1,20))

def get_dns_maxdns():
    # Maximum length of hostname when uploading data over DNS (0-255)
    return str(random.randint(240,254))

def get_dns_host():
    # Random dns host using this format string.string.
    length = random.randint(1,7)
    return get_random_alphanum(length) + "."

def get_ssh_banner():
    # Return random SSH banner (not guaranteed to real)
    return "SSH-2.0-OpenSSH_" + str(random.randint(4,9)) + "." + str(random.randint(1,9)) + "p" + str(random.randint(0,9)) + " " + str(random.choice(["Debian","Linux","RedHat","CentOS","Ubuntu"]))

def get_http_server_headers():
    # Header: Server
    servers = ['Apache','nginx', 'ESF','cloudflare','gsw','CloudFront', 'Node.js','Microsoft-IIS/10.0','AkamaiGHost','Google Frontend']
    return random.choice(servers)

def get_http_server_contenttype():
    # 
    contenttypes = ["application/javascript","plain/text","application/json"]
    return '"Content-Type" "' + random.choice(contenttypes) + '; charset=utf-8"'

def get_post_ex_spawnto_x86():
    targets = ['svchost.exe -k netsvc','svchost.exe -k wksvc','Locator.exe','systray.exe','WUAUCLT.exe','w32tm.exe','dllhost.exe -o enable','DevicePairingWizard.exe','getmac.exe /V','grpconv.exe','EhStorAuthn.exe','dns-sd.exe']
    target = random.choice(targets)
    return '%windir%\\\\syswow64\\\\' + target

def get_post_ex_spawnto_x64():
    targets = ['svchost.exe -k netsvc','svchost.exe -k wksvc','Locator.exe','systray.exe','WUAUCLT.exe','w32tm.exe','dllhost.exe -o enable','DevicePairingWizard.exe','getmac.exe /V','grpconv.exe','EhStorAuthn.exe','dns-sd.exe']
    target = random.choice(targets)
    return '%windir%\\\\sysnative\\\\' + target

def get_post_ex_pipename_list():
    names =  'ProtectionManager_##, Winsock2\\\\CatalogChangeListener-##-##, Spool\\\\pipe_##, WkSvcPipeMgr_##, NetClient_##, RPC_##, WiFiNetMgr_##, AuthPipeD_##'
    return names

def get_stage_allocator():
    # Set how Beacon's Reflective Loader allocates memory for the agent. Options are: HeapAlloc, MapViewOfFile, and VirtualAlloc.
    options = ["VirtualAlloc","HeapAlloc","MapViewOfFile"]
    allocator = random.choice(options)
    rwx = "false"
    if (allocator == "HeapAlloc"):
        rwx = "true"
    allocator_settings = '''
    set allocator      "{0}";
    set userwx         "{1}";
    '''.format(allocator,rwx)
    return allocator_settings

def get_stage_magic_pe():
    # Override the PE character marker used by Beacon's Reflective Loader with another value.
    return get_random_string(2)
    
def get_stage_compile_time():
    month  = random.choice(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    day    = str(random.randint(1,30)).zfill(2)
    year   = str(random.choice(range(2005,2020)))
    hour   = str(random.randint(1,23)).zfill(2)
    minute = str(random.randint(1,59)).zfill(2) 
    second = str(random.randint(1,50)).zfill(2) 
    return day + " " + month + " " + year + " " + hour + ":" + minute + ":" + second

def get_stage_entry_point():
    # The EntryPoint value in Beacon's PE header
    low = 300000
    high = 800000
    return str(random.randint(low,high))

def get_stage_image_size_x86():
    # SizeOfImage value in x86 Beacon's PE header.
    low = 512001
    high = 576000
    return str(random.randint(low,high))

def get_stage_image_size_x64():
    # SizeOfImage value in x64 Beacon's PE header.
    low = 512001
    high = 576000
    return str(random.randint(low,high))

def get_stage_name():
    # The Exported name of the Beacon DLL
    return get_random_object() + ".dll"


def get_stage_rich_header():
    # https://blog.cobaltstrike.com/2018/04/09/cobalt-strike-3-11-the-snake-that-eats-its-tail/
    # https://securelist.com/the-devils-in-the-rich-header/84348/
    # |        |                        |                    |                             |
    # | ------ | ---------------------- | ------------------ | --------------------------- |
    # | Offset | First value            | Second value       | Description                 |
    # | 00     | 44 61 6E 53 (“DanS”)   | 00 00 00 00        | Beginning of the header     |
    # | 08     | 00 00 00 00            | 00 00 00 00        | Empty record                |
    # | 10     | Tool id, build version | Number of items    | Bill of materials record #1 |
    # | …      |                        |                    |                             |
    # | …      | 52 69 63 68 “Rich”     | Checksum / XOR key | End of the header           |


    DanS = "\\x" + "\\x".join(["44","61","61","53"])
    DansS_second = "\\x" + "\\x".join(["00","00","00","00"])
    offset08 = "\\x" + "\\x".join(["00","00","00","00"])
    offset08_second = "\\x" + "\\x".join(["00","00","00","00"])
    content = get_random_bytearry(72) # 72 bytes
    Rich = "\\x" + "\\x".join(["52","69","63","68"])
    End1 = "\\x" + "\\x".join(["7a","f9","90","26"])
    End2 = "\\x" + "\\x".join(["00","00","00","00"])
    End3 = "\\x" + "\\x".join(["00","00","00","00"])
    End4 = "\\x" + "\\x".join(["00","00","00","00"])
    #rich_header = str(DanS) + DansS_second + offset08 + offset08_second + content + Rich + End1 + End2
    rich_header = str(DanS) + DansS_second + offset08 + offset08_second + content + Rich + End1 + End2 + End3 + End4
    return rich_header

def get_process_inject_allocator():
    # The preferred method to allocate memory in the remote process. Specify VirtualAllocEx or NtMapViewOfSection. The NtMapViewOfSection option is for same-architecture injection only. VirtualAllocEx is always used for cross-arch memory allocations.
    options = ['VirtualAllocEx', 'NtMapViewOfSection']
    return random.choice(options)

def get_process_inject_min_alloc():
    # Minimum amount of memory to request for injected content
    low = 4096
    high = 20480
    return str(random.randint(low,high))

def get_process_inject_execute():
    # execute block controls the methods Beacon will use when it needs to inject code into a process. 
    execute_string = '''
        CreateThread "ntdll!RtlUserThreadStart+0x{0}";
        CreateThread;
        NtQueueApcThread-s;
        CreateRemoteThread;
        RtlCreateUserThread; 
    '''.format(random.randint(42,1000))
    return execute_string

def get_http_config_headers():
    # Header: Server
    servers = ['Apache','nginx', 'ESF','cloudflare','gsw','CloundFront', 'Node.js','Microsoft-IIS/10.0','AkamaiGHost','Google Frontend']
    return random.choice(servers)

def get_http_client_metadata_cookie():
    cookie_prefixes = [
                        "_" + get_random_string(2) + "id", 
                        'SESSIONID_' + get_random_alphanum(random.randint(8,32)), 
                        'secure_id_' + get_random_alphanum(random.randint(8,32)), 
                        'auth_token' + get_random_alphanum(4), 
                        'affiliate_id_' + get_random_alphanum(16),
                        get_random_alphanum(random.randint(2,4)) +"_" + get_random_alphanum(32)
                      ]
    cookie = random.choice(cookie_prefixes) + "="
    return cookie

def get_http_post_client_id_parameter():
    return "_" + get_random_string(8)