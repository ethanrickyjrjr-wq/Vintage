# contract probe: ntfy.sh publish to a random throwaway topic, 2026-10-26

## POST https://ntfy.sh/hvprobe<random>  -H 'Title: Probe' -H 'Priority: high' -H 'Click: https://example.com/x' -H 'Tags: warning,lamp'  -d 'contract probe, ignore'
(first attempt returned an empty body, retry succeeded; transient)

HTTP/1.1 200 OK
Content-Type: application/json

{"id":"YzaLiP58E5FV","time":1793043465,"expires":1793086665,"event":"message","topic":"hvprobe179304346210566","title":"Probe","message":"contract probe, ignore","priority":4,"tags":["warning","lamp"],"click":"https://example.com/x"}

Reading: Priority "high" echoed as priority 4; Title, Tags (array), Click all accepted. Message retained: expires - time = 43200 s (12 h).
