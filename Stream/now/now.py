import re
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.plugin.api import validate
from streamlink.stream.hls import HLSStream

@pluginmatcher(re.compile(
    r"https?://(?:www\.)?nowtv\.com\.tr/"
))
class NowTVTR(Plugin):
    def _get_streams(self):
        # Hole den HTML-Inhalt der Webseite
        site_content = self.session.http.get(self.url).text
        
        # Extrahiere die daionUrl für den Live-Stream
        stream_url = self._extract_live_url(site_content)
        
        # Falls eine URL gefunden wurde, parse die HLS Streams
        if stream_url:
            return HLSStream.parse_variant_playlist(self.session, stream_url)

    def _extract_live_url(self, content):
        # Regulärer Ausdruck, um die URL aus dem JavaScript-Code zu extrahieren
        match = re.search(r'daionUrl\s*:\s*"(https[^"]+)"', content)
        if match:
            return match.group(1)
        else:
            self.logger.error("Live URL not found in the content.")
            return None

__plugin__ = NowTVTR
