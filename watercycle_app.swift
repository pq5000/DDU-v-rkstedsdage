import SwiftUI

struct ContentView: View {
    private let webhookURL = "Censoreret af sikkerhedsmæssige årsager"

    @State private var timerEnabled = false
    @State private var days = 0
    @State private var hours = 0
    @State private var minutes = 0

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            VStack(spacing: 30) {
                Text("💐")
                    .font(.system(size: 100))

                Button("Start Water Cycle") {
                    sendMessage("w")
                }
                .buttonStyle()

                Toggle("Timer Mode", isOn: $timerEnabled)
                    .foregroundColor(.white)
                    .padding(.horizontal, 40)
                    .onChange(of: timerEnabled) { value in
                        sendMessage(value ? "timer on" : "timer off")
                    }

                if timerEnabled {
                    VStack(spacing: 15) {
                        Stepper("Days: \(days)", value: $days, in: 0...30)
                        Stepper("Hours: \(hours)", value: $hours, in: 0...23)
                        Stepper("Minutes: \(minutes)", value: $minutes, in: 0...59)
                    }
                    .foregroundColor(.white)
                    .padding(.horizontal, 40)

                    Button("Set Interval") {
                        sendMessage("time \(days) \(hours) \(minutes)")
                    }
                    .buttonStyle()
                }
            }
        }
    }

    func sendMessage(_ content: String) {
        guard let url = URL(string: webhookURL) else { return }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body = ["content": content]
        request.httpBody = try? JSONSerialization.data(withJSONObject: body)

        URLSession.shared.dataTask(with: request).resume()
    }
}

extension Button {
    func buttonStyle() -> some View {
        self
            .fontWeight(.semibold)
            .frame(maxWidth: .infinity)
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(10)
            .padding(.horizontal, 40)
    }
}

@main
struct DiscordWebhookApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
