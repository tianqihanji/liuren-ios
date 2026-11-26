import SwiftUI
import WebKit

struct LiuRenWebView: UIViewRepresentable {

    func makeUIView(context: Context) -> WKWebView {
        let cfg = WKWebViewConfiguration()
        cfg.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")
        cfg.defaultWebpagePreferences.allowsContentJavaScript = true

        let wv = WKWebView(frame: .zero, configuration: cfg)
        wv.isOpaque = false
        wv.backgroundColor = UIColor(red: 0.027, green: 0.039, blue: 0.071, alpha: 1)
        wv.scrollView.contentInsetAdjustmentBehavior = .never
        wv.allowsBackForwardNavigationGestures = false

        if let url = Bundle.main.url(forResource: "index", withExtension: "html") {
            wv.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
        }
        return wv
    }

    func updateUIView(_ uiView: WKWebView, context: Context) {}
}

@main
struct LiuRenApp: App {
    var body: some Scene {
        WindowGroup {
            LiuRenWebView()
                .ignoresSafeArea(.all)
                .preferredColorScheme(.dark)
        }
    }
}
